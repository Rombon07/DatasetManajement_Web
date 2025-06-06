from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
]
