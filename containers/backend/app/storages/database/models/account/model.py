from storages.database.models.account.pydantic_model import AccountModel
from storages.database.models.base.base import DeletingBase


class Account(AccountModel, DeletingBase, table=True):
    pass
