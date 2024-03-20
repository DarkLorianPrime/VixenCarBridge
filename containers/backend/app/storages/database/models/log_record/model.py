from storages.database.models.base.base import DeletingBase
from storages.database.models.log_record.pydantic_model import AuditLog


class AuditRecord(AuditLog, DeletingBase, table=True):
    pass
