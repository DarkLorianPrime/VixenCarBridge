from enum import Enum
from os import getenv
from typing import AsyncGenerator, Generator

from sqlalchemy import URL, create_engine, Engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlalchemy.orm import sessionmaker, Session
from sqlmodel.ext.asyncio.session import AsyncSession


class Drivers(Enum):
    async_driver = "asyncpg"
    driver = "psycopg2"


url = URL(
    drivername=f"postgresql+{Drivers.async_driver.value}",
    username=getenv("POSTGRES_USER"),
    password=getenv("POSTGRES_PASSWORD"),
    host=getenv("POSTGRES_HOST"),
    database=getenv("POSTGRES_NAME"),
    port=5432,
    query={}
)

sync_url = URL(
    drivername=f"postgresql+{Drivers.driver.value}",
    username=getenv("POSTGRES_USER"),
    password=getenv("POSTGRES_PASSWORD"),
    host=getenv("POSTGRES_HOST"),
    database=getenv("POSTGRES_NAME"),
    port=5432,
    query={}
)
engine: AsyncEngine = create_async_engine(url, echo=True)
asyncsession_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

sync_engine: Engine = create_engine(sync_url, echo=True)
syncsession_maker = sessionmaker(bind=sync_engine, expire_on_commit=True, class_=Session)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with asyncsession_maker() as session:
        yield session


def get_session_sync() -> Generator[Session, None, None]:
    with syncsession_maker() as session:
        yield session