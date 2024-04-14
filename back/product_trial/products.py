from flask import Blueprint

bp = Blueprint("products", __name__, url_prefix="/products")

@bp.route("", methods=("GET", "POST"))
def product_repository():
    return "hello"
