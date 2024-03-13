import uuid
from http import HTTPMethod, HTTPStatus
from typing import Annotated, Optional, Any

from sqlalchemy import insert
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from storages.database.database import get_session
from storages.database.models.log_record.model import AuditRecord


class LoggerRepository:
    def __init__(self, session: Annotated[AsyncSession, get_session()]):
        self.session = session

    async def create(
            self,
            status_code: HTTPStatus,
            ip_address: str,
            user_id: Optional[uuid.UUID],
            action: Optional[HTTPMethod],
            endpoint: str,
            handle_time: float,
            exception: Optional[str],
            returning: Any = False
    ):
        stmt = (
            insert(AuditRecord)
            .values(
                status_code=status_code.value,
                ip_address=ip_address,
                user_id=user_id,
                action=None if action is None else action.value,
                endpoint=endpoint,
                handle_time=handle_time,
                exception=exception
            )
        )

        if returning:
            stmt = stmt.returning(returning)

        result = await self.session.execute(stmt)
        return result

    async def get(
            self,
            offset: int = 0,
            limit: int = 100,
            user_id: Optional[uuid.UUID] = None,
            one: bool = False
    ):
        queries: list[bool] = []

        if user_id:
            queries.append(AuditRecord.user_id == user_id)

        stmt = (
            select(AuditRecord)
            .filter(*queries)
            .order_by(AuditRecord.id)
            .limit(limit)
            .offset(offset)
        )

        result = await self.session.execute(stmt)

        scalar_result = result.scalars()

        if one:
            return scalar_result.first()

        return scalar_result.all()

    async def update(self):
        raise NotImplementedError()

    async def delete(self):
        # set removed
        raise NotImplementedError()
