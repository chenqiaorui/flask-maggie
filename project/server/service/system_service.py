# -*- coding: utf-8 -*-
from project.server.model.system_model import SystemModel
from project.server.utils.app_exception import AppException


def get_system_config():
    """
    获取系统配置
    :return:
    """
    rows = SystemModel.select()

    config = {}
    for row in rows:
        print(row.value)
        config[row.key] = row.value

    return config


def check_email_config(config):

    if not config['mail_host']:
        raise AppException('未设置发件邮箱服务器地址')

    if not config['mail_port']:
        raise AppException('未设置发件邮箱服务器端口')

    if not config['mail_username']:
        raise AppException('未设置发件人邮箱账号')

    if not config['mail_password']:
        raise AppException('未设置发件人邮箱密码')
