# from django.urls import url
from django.urls import include, path

from .views import *
app_name = "users"

urlpatterns = [
    path("register/", SignUpApiView.as_view(), name="register"),
    path("login/", CustomAuthToken.as_view(), name="login"),
] 