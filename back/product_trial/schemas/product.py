from marshmallow_sqlalchemy import auto_field

from product_trial.models.product import Product

from . import ma


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

    id = auto_field(dump_only=True)
    inventory_status = auto_field(data_key="inventoryStatus")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
