from django.urls import path
from . import views

urlpatterns = [
    path ("login/", views.Login_view, name="login"),
    path ("logout/", views.Logout_view, name="logout"),
]
