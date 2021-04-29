from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chattingapp import consumer

ws_pattern = [
    # To set up the websocket routing
    path("ws",consumer.TableData),
    path("wschat/<str:id>",consumer.NewTableData),

]

application = ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(ws_pattern))
    }
)