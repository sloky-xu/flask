from flask import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1

    # 蓝图注册到app核心对象上
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprints(app)

    return app

