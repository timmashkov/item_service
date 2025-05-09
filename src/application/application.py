from application.config import settings
from application.container import Container
from application.server import ApiServer
from presentation.api.item_router import ItemRouter

item_app = ApiServer(
    name=settings.NAME,
    routers=[
        ItemRouter().api_router,
    ],
    start_callbacks=[
        Container.broker_process_manager().start_broker_process,
        Container.rabbit_manager().connect,
        Container.rabbit_manager().init_queues,
    ],
    stop_callbacks=[Container.broker_process_manager().stop_broker_process],
).app
