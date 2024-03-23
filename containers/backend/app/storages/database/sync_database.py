from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from config.settings import settings

sync_engine: Engine = create_engine(settings.get_database_url(is_sync=True), echo=settings.DEBUG)
syncsession_maker = sessionmaker(bind=sync_engine, expire_on_commit=True, class_=Session)


def get_session_sync() -> Generator[Session, None, None]:
    with syncsession_maker() as session:
        yield session
