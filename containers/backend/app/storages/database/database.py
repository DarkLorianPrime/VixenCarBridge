from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession

from config.settings import settings


engine: AsyncEngine = create_async_engine(settings.get_database_url(is_sync=False), echo=settings.DEBUG)
asyncsession_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with asyncsession_maker() as session:
        yield session
