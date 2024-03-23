import logging

from config.settings import settings
from utils.logger.handler import SaveHandler

logging.basicConfig(level=settings.LOG_LEVEL)

db_logger = logging.getLogger('database')  # logger for database access
access_logger = logging.getLogger('access')  # logger for user access
access_logger.addHandler(SaveHandler())