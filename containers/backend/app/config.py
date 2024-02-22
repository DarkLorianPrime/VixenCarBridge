import logging

from utils.handlers.logger import SaveHandler

logging.basicConfig(level=logging.DEBUG, handlers=[SaveHandler()])

db_logger = logging.getLogger('database')  # logger for database access
access_logger = logging.getLogger('access')  # logger for user access
