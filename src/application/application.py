from application.config import settings
from application.container import Container
from application.server import ApiServer


item_app = ApiServer(
    name=settings.NAME,
    routers=[],
    start_callbacks=[
        Container.broker_process_manager().start_broker_process,
        Container.rabbit_manager().connect,
        Container.rabbit_manager().init_queues,
    ],
    stop_callbacks=[Container.broker_process_manager().stop_broker_process],
).app
