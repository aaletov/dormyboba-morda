from django.urls import path

from .views import IndexView, RegisterUser

urlpatterns = [
    path("widget", IndexView.as_view(), name="index"),
    path("registerUser", RegisterUser.as_view(), name="register-user"),
]
