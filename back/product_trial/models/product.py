from sqlalchemy.orm import Mapped, mapped_column

from . import db


class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[float]
    inventory_status: Mapped[str]
    category: Mapped[str]
    image: Mapped[str | None]
    rating: Mapped[float | None]
