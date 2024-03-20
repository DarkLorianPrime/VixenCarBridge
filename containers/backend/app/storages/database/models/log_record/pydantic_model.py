import uuid
from http import HTTPStatus, HTTPMethod
from typing import Any, Optional

from sqlmodel import SQLModel


class AuditLog(SQLModel):
    status_code: HTTPStatus
    ip_address: str
    user_id: Optional[uuid.UUID] = None
    action: Optional[HTTPMethod] = None
    endpoint: str
    handle_time: float
    exception: Optional[str] = None


class CreateAuditLog(AuditLog):
    returning: Any = False
