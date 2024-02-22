from fastapi import FastAPI, APIRouter
from starlette.requests import Request

app = FastAPI(
    title="VixenCarBridge",
)

main_router = APIRouter(prefix="/api/v1", tags=["Vixen CarBridge"])


@main_router.get("/status")
async def pong(request: Request):
    print(request.headers)
    return "ok"

app.include_router(main_router)
