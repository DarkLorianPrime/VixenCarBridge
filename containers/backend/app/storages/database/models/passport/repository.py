from typing import Annotated

from fastapi import Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from storages.database.database import get_session
from storages.database.models.passport.model import Passport
from storages.database.models.passport.pydantic_model import PassportModel


class PassportRepository:
    def __init__(
            self,
            session: Annotated[AsyncSession, Depends(get_session)]
    ):
        self.session = session

    async def create(
            self,
            payload: PassportModel
    ):
        data = payload.dict()
        returning = data.pop("returning")
        stmt = (
            insert(Passport)
            .values(**data)
        )
        
        if returning:
            stmt = stmt.returning(returning)
        
        result = await self.session.execute(stmt)
        await self.session.commit()
        
        if returning:
            scalars = result.scalars()
            return scalars.first()
        
        return result

    def get(self):
        ...

    def delete(self):
        # set removed
        ...
