from project.server.model.domain_model import DomainModel


def add(data):
    """
    添加域名
    :param data: {
        'domain': '必传',
     }
    :return:
    """
    domain = data['domain']
    row = DomainModel.create(
        domain=domain
    )
    return row

