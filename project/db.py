import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False,
            isolation_level=None
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


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    load_fixture()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
