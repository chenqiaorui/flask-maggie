# -*- coding: utf-8 -*-
import os
from flask import request, g

from project.server.model.user_model import UserModel
from project.server.service import token_service
from project.server.utils.app_exception import UnauthorizedAppException, ForbiddenAppException

# 白名单
WHITE_LIST = [
    '/api/login',
    '/api/register',
    '/apidocs'
]

# 仅管理账号可访问的接口
ADMIN_API_LIST = [
    # 全局配置管理
    '/api/tasks'
]

API_PREFIX = '/api'


def check_permission():
    # 仅校验api
    if not request.path.startswith(API_PREFIX) or request.path.startswith("/apidocs"):
        return

    # 白名单直接通过
    if request.path in WHITE_LIST:
        return

    # 获取token
    token = request.headers.get(os.getenv('TOKEN_KEY'))
    if not token:
        raise UnauthorizedAppException()

    # 解析token，并全局挂载
    payload = token_service.decode_token(token)
    g.user_id = payload['user_id']

    # root 权限 api
    if request.path in ADMIN_API_LIST:
        user_row = UserModel.get_by_id(g.user_id)

        if user_row.username != os.getenv('ADMIN_USERNAME'):
            raise ForbiddenAppException()
