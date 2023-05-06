from flask import request, jsonify, g

from project.server.service import domain_service
from project.server.model.domain_model import DomainModel
from playhouse.shortcuts import model_to_dict


def add_domain():
    """
    添加域名
    :return:
    """
    domain = request.json['domain']

    row = domain_service.add({'domain': domain})

    return {'id': row.id}

def get_domain_list():
    """
    获取域名列表
    :return:
    """
    current_user_id = g.user_id

    page = request.json.get('page', 1)
    size = request.json.get('size', 10)
    keyword = request.json.get('keyword')
    
    query = DomainModel.select().where(
        DomainModel.id == current_user_id
    )
    
    if keyword:
        query = query.where(DomainModel.domain.contains(keyword))

    ordering = []
    ordering.append(DomainModel.id.desc())

    lst = query.order_by(*ordering).paginate(page, size)
    total = query.count()
    print(lst)
    lst = list(map(lambda m: model_to_dict(
        model=m,
        extra_attrs=[
            'domain',
        ]
    ), lst))

    return {
        'list': lst,
        'total': total
    }

