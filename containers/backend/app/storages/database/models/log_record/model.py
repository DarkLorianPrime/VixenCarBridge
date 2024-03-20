import uuid

from sqlmodel import Field

from storages.database.models.base.base import DeletingBase


class AuditRecord(DeletingBase, table=True):
    status_code: int
    ip_address: str
    user_id: uuid.UUID | None = Field(foreign_key="account.id", nullable=True)
    action: str | None
    endpoint: str
    handle_time: float
    exception: str | None
