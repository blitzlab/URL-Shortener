from django.contrib import admin
from main.views import url_redirect
from django.urls import path, include
from django.views.generic import TemplateView



urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include('main.urls', namespace="main")),
    path(r'<str:url_code>/', url_redirect, name="redirect"),
    path(r'', TemplateView.as_view(template_name="index.html")),
]
