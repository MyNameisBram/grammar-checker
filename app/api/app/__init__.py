from flask import Flask
import os

from config import Config
from app.extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    template_dir = os.path.abspath("./templates")

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
