from django.urls import path, re_path
from drawing_app import consumers

websocket_urlpatterns = [
    re_path(r"ws/drawing_board/(?P<room_name>\w+)/$", consumers.DrawingBoardConsumer.as_asgi()),
]