from typing import Optional

from httpx import AsyncClient

from infrastructure.common.base_entities.singleton import Singleton


class UserHTTPService(Singleton):
    def __init__(self, prefix: str, port: int, host: str = "localhost") -> None:
        self._url: str = f"http://{host}:{port}/{prefix}"

    async def get_user(self, user_uuid: str) -> Optional[dict]:
        url = self._url + f"/{user_uuid}"
        async with AsyncClient() as client:
            answer = await client.get(url=url)
        return answer.json() if answer else None
