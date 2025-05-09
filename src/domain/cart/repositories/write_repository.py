from adapters.database.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Cart
from infrastructure.database.repositories.write_repository import WriteRepository


class CartWriteRepository(WriteRepository):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Cart)
