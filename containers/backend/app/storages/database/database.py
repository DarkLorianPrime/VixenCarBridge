from os import getenv
from typing import AsyncGenerator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlalchemy.util import immutabledict
from sqlmodel.ext.asyncio.session import AsyncSession

url = URL(
    drivername="postgresql+asyncpg",
    username=getenv("POSTGRES_USER"),
    password=getenv("POSTGRES_PASSWORD"),
    host=getenv("POSTGRES_HOST"),
    database=getenv("POSTGRES_NAME"),
    port=5432,
    query=immutabledict({"application_name": "VixenCarBridge"})
)

engine: AsyncEngine = create_async_engine(url, echo=True, future=True)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session
