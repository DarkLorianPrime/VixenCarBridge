from enum import Enum


class Drivers(Enum):
    ASYNC_DRIVER = "asyncpg"
    DRIVER = "psycopg2"
