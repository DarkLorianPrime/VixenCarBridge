import uuid
from typing import Annotated, Optional

from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from storages.database.database import get_session
from storages.database.models.log_record.model import AuditRecord


class LoggerRepository:
    def __init__(self, session: Annotated[AsyncSession, get_session()]):
        self.session = session

    async def create(self):
        raise NotImplementedError()

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
