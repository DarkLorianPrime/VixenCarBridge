from enum import Enum


class Drivers(Enum):
    async_driver = "asyncpg"
    driver = "psycopg2"