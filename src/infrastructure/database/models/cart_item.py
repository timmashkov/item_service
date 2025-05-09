import uuid

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from infrastructure.database.models import Base

if TYPE_CHECKING:
    from infrastructure.database.models.cart import Cart
    from infrastructure.database.models.item import Item


class CartItem(Base):

    __table_args__ = (
        UniqueConstraint("cart_id", "item_id", name="idx_unique_cart_item"),
    )

    cart_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("carts.uuid", ondelete="CASCADE"),
        nullable=False, index=True,
        comment="Ссылка на корзину"
    )
    item_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("items.uuid"),
        nullable=False, index=True,
        comment="Ссылка на товар"
    )
    quantity: Mapped[int] = mapped_column(
        default=1,
        comment="Количество товара"
    )

    cart: Mapped["Cart"] = relationship(
        back_populates="items"
    )
    item: Mapped["Item"] = relationship(
        back_populates="cart_items"
    )
