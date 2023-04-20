import os

from flask import Flask
from flask_mysqldb import MySQL
from flask_mail import Mail
from dotenv import load_dotenv

from project.server.router import api_map
from project.server.utils import permission
from project.server.utils import register, swagger
from flasgger import Swagger, NO_SANITIZER

from project.server.utils.swagger import template, swagger_config

mysql = MySQL()
mail = Mail()


def init_mysql(app):
    mysql.init_app(app)

    load_dotenv()  # take environment variables from .env.

    # Mysql Settings
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'root'
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'faztpassword'
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or '127.0.0.1'  # localhost
    app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT')) or 3306
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'flaskcrud'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


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

    # 初始化数据库
    init_mysql(app)

    # 初始化mail
    init_mail(app)

    # register blueprints
    # from project.server.main.views import main_blueprint
    # from project.server.contract.views import contract_blueprint
    #
    # app.register_blueprint(main_blueprint)
    # app.register_blueprint(contract_blueprint)

    # 路由
    register.register_app_routers(app, api_map.routes)

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    @app.before_request
    def before_request():
        permission.check_permission()

    return app


