from logging import Handler, LogRecord


class SaveHandler(Handler):
    def emit(self, record: LogRecord):
        print(record.msg, "LOG")
