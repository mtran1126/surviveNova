
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("character/", views.character, name="character"),
    path("stats/", views.stats, name="stats"),
]
