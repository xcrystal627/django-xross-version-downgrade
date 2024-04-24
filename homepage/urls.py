from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('send_mail', views.send_mail, name='send_mail'),
]