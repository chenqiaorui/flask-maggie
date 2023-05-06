from project.server.model.base_model import BaseModel
from peewee import CharField, IntegerField

class DomainModel(BaseModel):
    """域名"""
    id = IntegerField(primary_key=True)

    # 域名
    domain = CharField()

    class Meta:
        table_name = 'domain'

