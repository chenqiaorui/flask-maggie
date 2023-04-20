from flask import request, g
import json

from project.server.model.notify_model import NotifyModel
from project.server.service import notify_service


def update_notify_of_user():
    """
    更新用户通知配置
    :return:
    """
    current_user_id = g.user_id

    type_id = request.json['type_id']
    value = request.json['value']

    row = NotifyModel.get_or_none(
        NotifyModel.user_id == current_user_id,
        NotifyModel.type_id == type_id
    )

    value_raw = json.dumps(value, ensure_ascii=False)

    if row:
        NotifyModel.update(
            value_raw=value_raw
        ).where(
            NotifyModel.id == row.id
        ).execute()
    else:
        NotifyModel.create(
            user_id=current_user_id,
            type_id=type_id,
            value_raw=value_raw
        )


def test_webhook_notify_of_user():
    """
    测试webhook调用
    :return:
    """
    current_user_id = g.user_id

    return notify_service.notify_webhook_of_user(current_user_id)

