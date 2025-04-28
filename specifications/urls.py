from django.urls import path
from . import views

app_name = 'specifications'

urlpatterns = [
    path('', views.index, name='index'),
]
