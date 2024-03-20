import uuid
from datetime import datetime
from typing import Annotated, Optional, List

from sqlalchemy import insert
from sqlalchemy.orm import Session
from sqlmodel import select

from storages.database.sync_database import get_session_sync
from storages.database.models.log_record.model import AuditRecord
from storages.database.models.log_record.pydantic_model import AuditLog, CreateAuditLog


class LoggerRepository:
    def __init__(self, session: Annotated[Session, get_session_sync()]):
        self.session = session

    def create(
            self,
            payload: CreateAuditLog
    ):
        items = payload.dict()

        stmt = insert(AuditRecord).values(**items)

        if payload.returning:
            stmt = stmt.returning(payload.returning)

        result = self.session.execute(stmt)
        return result

    def get(
            self,
            offset: int = 0,
            limit: int = 100,
            user_id: Optional[uuid.UUID] = None,
            one: bool = False
    ):
        query_filters: list[bool] = []
        
        if user_id:
            query_filters.append(AuditRecord.user_id == user_id)

        stmt = (
            select(AuditRecord)
            .filter(*query_filters)
            .order_by(AuditRecord.id)
            .limit(limit)
            .offset(offset)
        )

        result = self.session.execute(stmt)
        
        scalar_result = result.scalars()
        
        if one:
            return scalar_result.first()

        return scalar_result.all()

    def delete(self, instance: AuditRecord):
        # set removed
        instance.removed = True
        instance.removed_at = datetime.now()
        
    def bulk_create(self, payload: List[AuditLog]):
        payload_list = [item.dict() for item in payload]
        self.session.bulk_insert_mappings(AuditRecord, payload_list)