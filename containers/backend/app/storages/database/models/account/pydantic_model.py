import uuid
from typing import Any

from sqlalchemy import Column
from sqlmodel import SQLModel, Field

from storages.database.types.file import File


class AccountModel(SQLModel):
    """
    primary:
        ├── email
        ├── username
    """
    email: str
    username: str
    password: str
    balance: float
    passport: uuid.UUID | None = Field(foreign_key='passport.id')
    avatar_url: str | None = Field(sa_column=Column(File(bucket="avatars"), nullable=True))


class CreateAccountModel(AccountModel):
    returning: Any = False
