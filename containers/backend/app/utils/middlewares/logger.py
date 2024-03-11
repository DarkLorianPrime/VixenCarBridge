import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class LoggerMiddleware(BaseHTTPMiddleware):
    async def on_response(
            self,
            request: Request,
            response: Response,
            duration: float,
    ):
        """
        :param request: request object:
            ip_address: str
            user_id: uuid.UUID | None
            action: str | None
            endpoint: str
            handle_time: float

        :param response: response object
            status_code: int

        :param duration: handle duration
        """
        log_data = {
            "status_code": response.status_code,
            "ip_address": request.headers.get("X-Real-IP"),
            "user_id": request.scope.get("user"),
            "action": request.method,
            "handle_time": duration,
            "endpoint": request.scope.get("route").path
        }
        print(log_data)

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()

        response = await call_next(request)

        if response.status_code == 307:
            return response

        duration = time.time() - start_time

        await self.on_response(request, response, duration=duration)

        return response
