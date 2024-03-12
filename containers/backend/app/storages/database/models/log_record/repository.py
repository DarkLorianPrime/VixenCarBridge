from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from storages.database.database import get_session


class PassportRepository:
    def __init__(self, session: Annotated[AsyncSession, get_session()]):
        self.session = session

    async def create(self):
        raise NotImplementedError()

    async def get(self):
        raise NotImplementedError()

    async def update(self):
        raise NotImplementedError()

    async def delete(self):
        # set removed
        raise NotImplementedError()
