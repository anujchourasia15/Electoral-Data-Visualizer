from django.urls import path
from .views import home , about

app_mame = "app"

urlpatterns = [
    path("home/", home),
    path("home/about/", about),
    path("home/about/home/", home),
]
