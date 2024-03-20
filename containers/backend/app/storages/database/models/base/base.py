import uuid
from datetime import datetime

from sqlmodel import SQLModel, Field


class Base(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, unique=True, nullable=False, index=True)
    created_at: datetime = Field(default_factory=datetime.now)


class DeletingBase(Base):
    removed: bool = Field(default=False)
    removed_at: datetime = Field(default=None, nullable=True)
