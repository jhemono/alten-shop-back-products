from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints
    from . import products
    app.register_blueprint(products.bp)

    return app
