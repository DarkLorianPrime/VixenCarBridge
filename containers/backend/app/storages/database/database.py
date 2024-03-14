from os import getenv
from typing import AsyncGenerator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession

from storages.database.enums import Drivers

url = URL(
    drivername=f"postgresql+{Drivers.async_driver.value}",
    username=getenv("POSTGRES_USER"),
    password=getenv("POSTGRES_PASSWORD"),
    host=getenv("POSTGRES_HOST"),
    database=getenv("POSTGRES_NAME"),
    port=5432,
    query={}
)

engine: AsyncEngine = create_async_engine(url, echo=True)
asyncsession_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with asyncsession_maker() as session:
        yield session
