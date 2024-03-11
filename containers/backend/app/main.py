from fastapi import FastAPI, APIRouter
from starlette.middleware import Middleware
from starlette.requests import Request

from utils.middlewares.logger import LoggerMiddleware

"""
To-Do:
add dependency function to set user scope
async def auth(request: Request):
    request.scope["user"] = "set in depend"

in app add:
    Depends(auth)
"""


app = FastAPI(
    title="VixenCarBridge",
    middleware=[Middleware(LoggerMiddleware)]
)

main_router = APIRouter(prefix="/api/v1", tags=["Vixen CarBridge"])


@main_router.get("/status")
async def pong(request: Request):
    print(request.scope)
    return "ok"

app.include_router(main_router)
