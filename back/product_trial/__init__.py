from flask import Flask

from product_trial.models import db
from product_trial.schemas import ma


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Initialize Marshmallow
    ma.init_app(app)

    # Register blueprints
    from . import products

    app.register_blueprint(products.bp)

    return app
