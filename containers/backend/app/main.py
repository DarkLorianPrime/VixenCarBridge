from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="VixenCarBridge",
)

main_router = APIRouter(prefix="/api/v1", tags=["Vixen CarBridge"])


@main_router.get("/hello")
async def pong():
    return "world"

app.include_router(main_router)
