import uuid

from sqlalchemy import Column
from sqlmodel import Field

from storages.database.models.base import Base
from storages.database.types.file import File


class Account(Base, table=True):
    email: str
    password: str
    balance: float
    avatar_url: str = Field(sa_column=Column(File(bucket="avatars")))
    passport: uuid.UUID = Field(foreign_key='passport.id')
