# -*- coding: utf-8 -*-
import logging
import os
from logging.handlers import RotatingFileHandler

from peewee import Model, MySQLDatabase
from dotenv import load_dotenv

# 打印日志
from project.server.service.file_service import resolve_log_file

logger = logging.getLogger('peewee')

# 单个日志文件最大为1M
handler = RotatingFileHandler(resolve_log_file("peewee.log"), maxBytes=1024 * 1024 * 1, encoding='utf-8')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# 连接到 MySQL 数据库
load_dotenv()  # take environment variables from .env.
db = MySQLDatabase(os.getenv('MYSQL_DB'), user=os.getenv('MYSQL_USER'), password=os.getenv('MYSQL_PASSWORD'),
                   host=os.getenv('MYSQL_HOST'), port=int(os.getenv('MYSQL_PORT')), charset='utf8mb4')


class BaseModel(Model):
    class Meta:
        database = db
