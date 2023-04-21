import json
import os
from datetime import datetime
import warnings
from project.server.model.base_model import BaseModel
from peewee import CharField, IntegerField, DateTimeField, BooleanField, TextField

from project.server.utils import bcrypt_util


class UserModel(BaseModel):
    """用户"""
    id = IntegerField(primary_key=True)

    # 用户名
    username = CharField(unique=True, null=None)

    # 密码
    password = CharField()

    # 头像
    avatar_url = CharField(null=None, default='')

    # 过期前多少天提醒
    before_expire_days = IntegerField(null=None, default=3)

    # 邮件列表
    # Deprecated 已弃用 v0.0.12
    email_list_raw = TextField(default=None, null=True)

    # 账号状态
    status = BooleanField(default=True)

    # 创建时间
    create_time = DateTimeField(default=datetime.now)

    # 更新时间
    update_time = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'user'

    @property
    def email_list(self):
        warnings.warn("UserModel field email_list is Deprecated, please use NotifyModel", DeprecationWarning)

        if self.email_list_raw:
            return json.loads(self.email_list_raw)
        else:
            return []

if __name__ == '__main__':
    # 插入数据
    UserModel.create(username='ricky', password='123456')

