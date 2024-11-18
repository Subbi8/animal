from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import animals, adoption, volunteers, scheduling
    app.register_blueprint(animals.bp)
    app.register_blueprint(adoption.bp)
    app.register_blueprint(volunteers.bp)
    app.register_blueprint(scheduling.bp)

    return app
