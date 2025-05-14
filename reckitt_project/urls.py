# reckitt_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reckitt_app/', include('reckitt_app.urls')),
    path('', RedirectView.as_view(pattern_name='reckitt_app:user_list'), name='home'),
]