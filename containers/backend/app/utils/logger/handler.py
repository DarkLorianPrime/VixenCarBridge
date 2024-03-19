from logging import Handler, LogRecord
from typing import List

from storages.database.sync_database import get_session_sync
from storages.database.models.log_record.pydantic_model import AuditLog
from storages.database.models.log_record.repository import LoggerRepository


class SaveHandler(Handler):
    def __init__(self, capacity: int = 256):
        super().__init__()
        self.capacity = capacity
        self.buffer: List[AuditLog] = []

    def save(self):
        """placeholder to save the buffer to the database"""
        session = next(get_session_sync())
        repo = LoggerRepository(session)
        repo.bulk_create(payload=self.buffer)
        session.commit()
        session.close()

    def flush(self):
        """save the buffer and flush it"""
        self.acquire()
        try:
            self.save()
            self.buffer.clear()
        finally:
            self.release()

    def emit(self, record: LogRecord):
        """Add information to the buffer and flush it if it has more than <capacity> records"""
        self.buffer.append(AuditLog.model_validate_json(record.msg))
        if len(self.buffer) >= self.capacity:
            self.flush()
