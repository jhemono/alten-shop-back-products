from flask import Blueprint, request
from flask.views import MethodView
from flask_restful import Api, Resource

from product_trial.models.product import Product, db
from product_trial.schemas.product import product_schema, products_schema

bp = Blueprint("products", __name__, url_prefix="/products")
api = Api(bp)


class ProductCatalogAPI(Resource):
    def get(self):
        products = db.session.execute(db.select(Product).order_by("id")).scalars()
        return products_schema.dump(products)

    def post(self):
        json_data = request.get_json()
        product = product_schema.load(json_data)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product)


class ProductAPI(MethodView):
    def get(self, id):
        product = db.get_or_404(Product, id)
        return product_schema.dump(product)

    def patch(self, id):
        product = db.get_or_404(Product, id)
        json_data = request.get_json()
        product_schema.load(json_data, instance=product, partial=True)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product)

    def delete(self, id):
        product = db.get_or_404(Product, id)
        db.session.delete(product)
        db.session.commit()
        return "OK"


api.add_resource(ProductAPI, "/<int:id>")
api.add_resource(ProductCatalogAPI, "")
