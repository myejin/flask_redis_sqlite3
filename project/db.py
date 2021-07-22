import redis 
import sqlite3
from flask import current_app, g


def get_redis():
    if "redis" not in g:
        g.redis = redis.from_url(
            current_app.config['REDIS_URL']
        )
    return g.redis    


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))
    current_app.logger.info("Database initialize done.")


def load_fixture():
    db = get_db()
    
    with current_app.open_resource("data.sql") as f:
        db.executescript(f.read().decode("utf8"))
    current_app.logger.info("Fixture load done.")


def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()
        load_fixture()
