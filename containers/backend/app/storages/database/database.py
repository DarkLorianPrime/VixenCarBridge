from os import getenv

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

url = URL(
    drivername="postgresql+asyncpg",
    username=getenv("POSTGRES_USER"),
    password=getenv("POSTGRES_PASSWORD"),
    host=getenv("POSTGRES_HOST"),
    database=getenv("POSTGRES_NAME"),
    port=5432,
    query={}
)

engine = create_async_engine(url, echo=True, future=True)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with session_maker() as session:
        yield session
