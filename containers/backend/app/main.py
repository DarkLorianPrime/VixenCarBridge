import atexit

from fastapi import FastAPI, APIRouter
from starlette.middleware import Middleware
from starlette.requests import Request

from config import access_logger
from utils.logger.middleware import LoggerMiddleware

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


@atexit.register
def force_save():
    access_logger.handlers[0].flush()
    
    
@main_router.get("/status")
async def pong(request: Request):
    print(request.scope)
    return "ok"


app.include_router(main_router)
