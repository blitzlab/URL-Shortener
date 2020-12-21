from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

app_name = "main"

# Main app urls
urlpatterns = [
    path(r"shorten", views.shorten_url, name="shortenurl"),
    path(r"signup", views.signup, name="signup"),
    path(r"login", obtain_auth_token, name="login"),
    path(r"urls", views.my_urls, name="myurls")
]
