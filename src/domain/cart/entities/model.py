from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from infrastructure.common.base_entities.patched_filter import PatchedFilter
from infrastructure.database.models import Cart


class CartIncomingData(BaseModel):
    user_uuid: UUID = Field(description=Cart.user_uuid.comment)


class CartResultData(CartIncomingData):
    uuid: UUID = Field(description=Cart.uuid.comment)
    created_at: datetime = Field(description=Cart.created_at.comment)
    updated_at: datetime = Field(description=Cart.updated_at.comment)


class CartFilter(PatchedFilter):
    uuid: Optional[UUID] = None
    user_uuid: Optional[UUID] = None

    class Constants(PatchedFilter.Constants):
        model = Cart
