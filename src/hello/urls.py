from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("lota", views.lota, name ="lota"),
    path("<str:name>", views.greet, name = "greet")
]