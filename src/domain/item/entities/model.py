from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from infrastructure.common.base_entities.patched_filter import PatchedFilter
from infrastructure.database.models import Item


class ItemIncomingData(BaseModel):

    name: str = Field(description=Item.name.comment)
    description: Optional[str] = Field(description=Item.description.comment)
    price: Decimal = Field(description=Item.price.comment)
    category: str = Field(description=Item.category.comment)
    is_available: bool = Field(description=Item.is_available.comment)


class ItemResultData(ItemIncomingData):
    uuid: UUID = Field(description=Item.uuid.comment)
    created_at: datetime = Field(description=Item.created_at.comment)
    updated_at: datetime = Field(description=Item.updated_at.comment)


class ItemFilter(PatchedFilter):
    uuid: Optional[UUID] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    is_available: Optional[bool] = None

    class Constants(PatchedFilter.Constants):
        model = Item
