
from django.urls import path

from . import views

urlpatterns = [
    path('set-chat',views.set_chat),
    path('get-all-chat',views.get_all_chat),
    path('signup',views.signup),
    path('signin',views.signin),
    path('new-connection',views.new_connection),
    path('friends',views.my_friends),
    path('chats',views.chats),
]