
from django.urls import path

from . import views

urlpatterns = [
    # path('get-formats',views.format),
    path('convert',views.convert),
    path('datasave',views.datasave),
    path('check',views.check),
    # path('addformat',views.massaddformat),

]
