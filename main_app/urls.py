from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_user, name="register"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
