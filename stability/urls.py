from django.urls import path
from . import views

app_name = 'stability'

urlpatterns = [
    path('', views.index, name='index'),
]
