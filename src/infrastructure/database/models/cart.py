import uuid

from typing import List, TYPE_CHECKING
from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models import Base

if TYPE_CHECKING:
    from infrastructure.database.models.cart_item import CartItem


class Cart(Base):

    user_uuid: Mapped[uuid.UUID] = mapped_column(
        UUID, nullable=False, index=True,
        comment="Идентификатор пользователя из user_service"
    )

    items: Mapped[List["CartItem"]] = relationship(
        back_populates="cart",
        cascade="all, delete-orphan"
    )
