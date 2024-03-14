import uuid
from http import HTTPStatus, HTTPMethod
from typing import Any, Optional

from pydantic import BaseModel

    
class AuditLog(BaseModel):
    status_code: HTTPStatus
    ip_address: str
    user_id: Optional[uuid.UUID] = None
    action: Optional[HTTPMethod] = None
    endpoint: str
    handle_time: float
    exception: Optional[str] = None
    returning: Any = False
