from flask import Flask

def create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_file, silent=True)
    from . import db
    db.init_app(app)

    from . import api 
    app.register_blueprint(api.bp)

    handle_error(app)
    return app 


def handle_error(app):
    @app.errorhandler(Exception)
    def db_error_handler(e):
        return {"error": str(e), "data": None}
