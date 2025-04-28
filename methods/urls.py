from django.urls import path
from . import views

app_name = 'methods'

urlpatterns = [
    path('', views.index, name='index'),
]
