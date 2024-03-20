import uuid
from typing import Annotated, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from storages.database.models.account.model import Account
from storages.database.models.base.repository import BaseRepository
from storages.database.sync_database import get_session_sync


class AccountRepository(BaseRepository):
    def __init__(self, session: Annotated[AsyncSession, get_session_sync()]):
        super().__init__(session, Account)
        self.session = session

    async def get(
            self,
            offset: int = 0,
            limit: int = 100,
            user_id: Optional[uuid.UUID] = None,
            one: bool = False
    ):
        query_filters: list[bool] = []

        if user_id:
            query_filters.append(Account.id == user_id)

        stmt = (
            select(Account)
            .filter(*query_filters)
            .order_by(Account.id)
            .limit(limit)
            .offset(offset)
        )

        result = await self.session.execute(stmt)

        scalar_result = result.scalars()

        if one:
            return scalar_result.first()

        return scalar_result.all()
