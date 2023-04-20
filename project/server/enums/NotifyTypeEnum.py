# -*- coding: utf-8 -*-


class NotifyTypeEnum(object):
    """
    通知方式枚举值
    """
    # 未知
    Unknown = 0

    # 邮件
    Email = 1

    # webHook
    WebHook = 2

    # 企业微信
    WORK_WEIXIN = 3