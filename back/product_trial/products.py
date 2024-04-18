from flasgger import swag_from
from flask import Blueprint, request
from flask_restful import Api, Resource

from product_trial.models.product import Product, db
from product_trial.schemas.product import ProductSchema, product_schema, products_schema

bp = Blueprint("products", __name__, url_prefix="/products")
api = Api(bp)


class ProductCatalogAPI(Resource):
    @swag_from(
        {
            "responses": {
                200: {
                    "description": "A list of products",
                    "schema": {
                        "type": "array",
                        "items": ProductSchema,
                    },
                }
            }
        }
    )
    def get(self):
        """Retrieve all products."""
        products = db.session.execute(db.select(Product).order_by("id")).scalars()
        return products_schema.dump(products)

    @swag_from(
        {
            "parameters": [
                {
                    "name": "body",
                    "in": "body",
                    "required": True,
                    "schema": ProductSchema,
                }
            ],
            "responses": {
                201: {
                    "description": "Resulting product data with id",
                    "schema": ProductSchema,
                }
            },
        }
    )
    def post(self):
        """Create a new products"""
        json_data = request.get_json()
        product = product_schema.load(json_data)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product), 201


class ProductAPI(Resource):
    @swag_from(
        {
            "responses": {
                200: {
                    "description": "Product data with id",
                    "schema": ProductSchema,
                },
                404: {"description": "Product doesn't exist"},
            }
        }
    )
    def get(self, id):
        """Retrieve details for a product"""
        product = db.get_or_404(Product, id)
        return product_schema.dump(product)

    @swag_from(
        {
            "responses": {
                200: {
                    "description": "Updated product data with id",
                    "schema": ProductSchema,
                },
                404: {"description": "Product doesn't exist"},
            }
        }
    )
    def patch(self, id):
        """Update details of product 1 if it exists"""
        product = db.get_or_404(Product, id)
        json_data = request.get_json()
        product_schema.load(json_data, instance=product, partial=True)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product)

    def delete(self, id):
        """Remove a product

        ---
        responses:
            204:
                description: Product was removed
            404:
                description: Product doesn't exist
        """
        product = db.get_or_404(Product, id)
        db.session.delete(product)
        db.session.commit()
        return None, 204


api.add_resource(ProductAPI, "/<int:id>")
api.add_resource(ProductCatalogAPI, "")
