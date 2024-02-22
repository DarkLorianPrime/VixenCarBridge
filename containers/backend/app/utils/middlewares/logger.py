from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class LoggerMiddleware(BaseHTTPMiddleware):
    async def on_request(self, request: Request):
        ...

    async def on_response(self, response: Response):
        ...

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        await self.on_request(request)

        response = await call_next(request)

        await self.on_response(response)

        return response
