from flask import Flask
import redis 

rq = redis.Redis()

def create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_file, silent=True)
    from . import db
    db.init_app(app)

    rq = redis.from_url(app.config['REDIS_URL'])

    from . import api 
    app.register_blueprint(api.bp)

    return app 