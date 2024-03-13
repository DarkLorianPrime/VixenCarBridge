from logging import Handler, LogRecord


class SaveHandler(Handler):
    def __init__(self, capacity: int = 256):
        super().__init__()
        self.capacity = capacity
        self.buffer = []

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

    def emit(self, record):
        """Add information to the buffer and flush it if it has more than <capacity> records"""
        self.buffer.append(record)
        if len(self.buffer) >= self.capacity:
            self.flush()
