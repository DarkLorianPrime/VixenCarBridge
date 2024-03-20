from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from storages.database.database import get_session
from storages.database.models.base.repository import BaseRepository
from storages.database.models.passport.model import Passport


class PassportRepository(BaseRepository):
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]):
        super().__init__(session, Passport)
