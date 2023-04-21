import os

from flask import Flask
from flask_mail import Mail

from project.server.router import api_map
from project.server.utils import permission
from project.server.utils import register, swagger
from flasgger import Swagger, NO_SANITIZER

from project.server.utils.swagger import template, swagger_config

mail = Mail()


def init_mail(app):
    # Mail Settings
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER') or 'smtp.qq.com'
    app.config['MAIL_PROT'] = int(os.getenv('MAIL_PROT')) or 465
    app.config['MAIL_USE_TLS'] = bool(os.getenv('MAIL_USE_TLS')) or True
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME') or '22@qq.com'
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD') or '22@qq.com'

    mail.init_app(app)


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder="../client/templates",
        static_folder="../client/static",
    )

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    app.debug = bool(os.getenv("FLASK_DEBUG"))

    # 配置swagger
    app.config["SWAGGER"] = {"title": "flask-maggie", "uiversion": 3}
    Swagger(app, sanitizer=NO_SANITIZER, template=template, config=swagger_config)

    # 初始化mail
    init_mail(app)

    # 路由
    register.register_app_routers(app, api_map.routes)

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    @app.before_request
    def before_request():
        permission.check_permission()

    return app


