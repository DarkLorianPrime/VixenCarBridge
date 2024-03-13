from logging import Handler, LogRecord
from typing import List



class SaveHandler(Handler):
    def __init__(self, capacity: int = 256):
        super().__init__()
        self.capacity = capacity
        self.buffer: List[LogRecord] = []

    def save(self):
        """placeholder to save the buffer to the database"""
        ...

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
        self.buffer.append(record)
        if len(self.buffer) >= self.capacity:
            self.flush()
