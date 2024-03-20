import json
from http import HTTPMethod, HTTPStatus
import time
from typing import Optional

from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint, _StreamingResponse
from starlette.requests import Request
from starlette.responses import Response

from config import access_logger


class LoggerMiddleware(BaseHTTPMiddleware):
    async def on_response(
            self,
            request: Request,
            status_code: HTTPStatus,
            exception: Optional[str],
            duration: float,
    ) -> None:
        """
        :param status_code: status code
        :param exception: if 4xx status - save his body
        :param request: request object:
            ip_address: str
            user_id: uuid.UUID | None
            action: str | None
            endpoint: str
            handle_time: float

        :param duration: handle duration
        """
        log_data = {
            "status_code": status_code,
            "ip_address": request.headers.get("X-Real-IP"),
            "user_id": request.scope.get("user"),
            "action": HTTPMethod[request.method],
            "exception": exception,
            "handle_time": duration,
            "endpoint": request.scope.get("route").path
        }
        access_logger.info(json.dumps(log_data))

    async def return_body(self, response: _StreamingResponse):
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        return json.loads(response_body[0].decode())["detail"]

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()

        response: _StreamingResponse | Response = await call_next(request)
        exception = None

        status_code = HTTPStatus(response.status_code)

        if status_code.is_redirection:
            return response

        if status_code.is_client_error:
            exception = await self.return_body(response)

        duration = time.time() - start_time

        await self.on_response(request, exception=exception, status_code=status_code, duration=duration)

        return response
