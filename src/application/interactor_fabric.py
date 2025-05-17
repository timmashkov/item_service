from contextlib import asynccontextmanager
from typing import AsyncContextManager

from fastapi import Depends

from application.container import Container
from application.interactors.checking_user import UserChecker
from application.services.user_service import UserHTTPService


class InteractorFactory:
    def __init__(
        self,
        user_service: UserHTTPService = Depends(Container.user_http_service),
    ) -> None:
        self.user_service = user_service

    @asynccontextmanager
    async def ensuring(
        self,
    ) -> AsyncContextManager[UserChecker]:
        yield UserChecker(
            user_service=self.user_service,
        )
