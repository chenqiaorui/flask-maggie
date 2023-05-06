from flask import request, jsonify

from project.server.service import domain_service


def add_domain():
    """
    添加域名
    :return:
    """
    domain = request.json['domain']

    row = domain_service.add({'domain': domain})

    return {'id': row.id}

