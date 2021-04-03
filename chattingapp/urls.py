
from django.urls import path

from . import views

urlpatterns = [
    path('set-chat',views.set_chat),
    path('get-all-chat',views.get_all_chat),
]