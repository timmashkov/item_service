from adapters.broker.rabbit_adapter import RabbitMQAdapter
from adapters.database.alchemy_adapter import AlchemyAdapter
from application.config import settings
from application.processes.consume_process import BrokerProcessManager
from domain.item.repositories.read_repository import ItemReadRepository
from domain.item.repositories.write_repository import ItemWriteRepository
from infrastructure.common.base_entities.singleton import OnlyContainer, Singleton


class Container(Singleton):

    alchemy_manager = OnlyContainer(
        AlchemyAdapter,
        dialect=settings.POSTGRES.dialect,
        host=settings.POSTGRES.host,
        login=settings.POSTGRES.login,
        password=settings.POSTGRES.password,
        port=settings.POSTGRES.port,
        database=settings.POSTGRES.database,
        echo=settings.POSTGRES.echo,
    )

    rabbit_manager = OnlyContainer(
        RabbitMQAdapter,
        **settings.RABBIT_MQ,
        queue_list=settings.RABBIT_ROUTING_KEYS,
    )

    broker_process_manager = OnlyContainer(
        BrokerProcessManager,
        broker=rabbit_manager(),
        queues=settings.RABBIT_ROUTING_KEYS,
    )

    item_write_manager = OnlyContainer(
        ItemWriteRepository,
        session_adapter=alchemy_manager(),
    )

    item_read_manager = OnlyContainer(
        ItemReadRepository,
        session_adapter=alchemy_manager(),
    )
