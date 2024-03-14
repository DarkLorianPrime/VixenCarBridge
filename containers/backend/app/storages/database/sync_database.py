from os import getenv
from typing import Generator

from sqlalchemy import Engine, create_engine, URL
from sqlalchemy.orm import Session, sessionmaker

from storages.database.enums import Drivers

sync_url = URL(
    drivername=f"postgresql+{Drivers.driver.value}",
    username=getenv("POSTGRES_USER"),
    password=getenv("POSTGRES_PASSWORD"),
    host=getenv("POSTGRES_HOST"),
    database=getenv("POSTGRES_NAME"),
    port=5432,
    query={}
)

sync_engine: Engine = create_engine(sync_url, echo=True)
syncsession_maker = sessionmaker(bind=sync_engine, expire_on_commit=True, class_=Session)


def get_session_sync() -> Generator[Session, None, None]:
    with syncsession_maker() as session:
        yield session