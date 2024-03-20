from storages.database.models.base.base import DeletingBase
from storages.database.models.passport.pydantic_model import PassportModel


class Passport(PassportModel, DeletingBase, table=True):
    ...
    
