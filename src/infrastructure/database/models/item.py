from decimal import Decimal
from typing import TYPE_CHECKING, List

from sqlalchemy import DECIMAL, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models import Base

if TYPE_CHECKING:
    from infrastructure.database.models.cart_item import CartItem


class Item(Base):

    name: Mapped[str] = mapped_column(
        String(100), nullable=False, comment="Название товара"
    )
    description: Mapped[str] = mapped_column(
        Text, nullable=True, comment="Описание товара"
    )
    price: Mapped[Decimal] = mapped_column(
        DECIMAL(10, 2), nullable=False, comment="Текущая цена товара"
    )
    category: Mapped[str] = mapped_column(
        String, nullable=False, comment="Категория товара"
    )
    is_available: Mapped[bool] = mapped_column(
        default=True, comment="Доступен ли товар для заказа"
    )

    cart_items: Mapped[List["CartItem"]] = relationship(back_populates="item")
