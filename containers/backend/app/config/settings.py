import logging

from pydantic_settings import BaseSettings

from storages.database.enums import Drivers
from sqlalchemy import URL


class Settings(BaseSettings):
    # postgres settings
    driver: str = "postgresql+"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_NAME: str
    port: int = 5432

    # logging settings
    LOG_LEVEL: str = logging.INFO
    debug: bool = False

    @classmethod
    def get_driver(cls, is_sync: bool = False):
        driver_part_2 = Drivers.DRIVER if is_sync else Drivers.ASYNC_DRIVER
        return cls.driver + driver_part_2.value

    @classmethod
    def get_database_url(cls, is_sync: bool = False):
        return URL(
            drivername=cls.get_driver(is_sync),
            username=cls.POSTGRES_USER,
            password=cls.POSTGRES_PASSWORD,
            host=cls.POSTGRES_HOST,
            database=cls.POSTGRES_NAME,
            port=cls.port,
            query={}
        )


settings = Settings()
