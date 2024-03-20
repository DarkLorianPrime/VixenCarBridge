from datetime import datetime
from typing import Annotated, Type

from fastapi import Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel

from storages.database.database import get_session
from storages.database.models.base.base import DeletingBase


class BaseRepository:
    def __init__(
            self,
            session: Annotated[AsyncSession, Depends(get_session)],
            model: Type[SQLModel]
    ):
        self.session = session
        self.model = model

    async def create(
            self,
            payload: Type[SQLModel]
    ):
        data = payload.dict()
        returning = data.pop("returning")

        stmt = insert(self.model).values(**data)
        if returning:
            stmt = stmt.returning(returning)

        result = await self.session.execute(stmt)

        if returning:
            scalars = result.scalars()
            return scalars.first()

        return result

    async def get(self):
        raise NotImplementedError()

    async def delete(self, instance: Type[DeletingBase]):
        instance.removed = True
        instance.removed_at = datetime.now()
