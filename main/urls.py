from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"

# Main app urls
urlpatterns = [
    path(r"shorten-url", views.shorten_url, name="shortenurl"),
]
