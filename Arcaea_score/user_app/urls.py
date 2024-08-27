from django.urls import path
from .views import login, logout, register, edit_password
urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("edit_password/", edit_password, name="edit_password"),
]