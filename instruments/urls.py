from django.urls import path
from . import views

app_name = 'instruments'

urlpatterns = [
    path('', views.index, name='index'),
]
