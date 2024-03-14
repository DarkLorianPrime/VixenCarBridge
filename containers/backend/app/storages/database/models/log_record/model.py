import uuid

from sqlmodel import Field

from storages.database.models.base import Base


class AuditRecord(Base, table=True):
    status_code: int
    ip_address: str
    user_id: uuid.UUID | None = Field(foreign_key="account.id", nullable=True)
    action: str | None
    endpoint: str
    handle_time: float
    exception: str | None
