from typing import Optional
from uuid import UUID

from application.services.user_service import UserHTTPService
from infrastructure.common.base_entities.base_interactor import BaseInteractor


class UserChecker(BaseInteractor[UUID, bool]):
    def __init__(
        self,
        user_service: UserHTTPService,
    ) -> None:
        self.user_service = user_service

    async def __call__(self, user_uuid: UUID) -> Optional[dict]:
        response = await self.user_service.get_user(user_uuid=str(user_uuid))
        return response
