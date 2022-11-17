# from django.conf.urls import url
from django.urls import include, path

from .views import *


urlpatterns = [
    path('menu/chicken_rep/', ChickenRepublicApi.as_view(), name='chicken_rep')
]