# reckitt_app/urls.py

from django.urls import path
from . import views

app_name = 'reckitt_app'

urlpatterns = [
    # LINE Webhook
    path('webhook/', views.LineWebhookView.as_view(), name='webhook'),
    
    # User Management
    path('', views.LineUserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', views.LineUserDetailView.as_view(), name='user_detail'),
    path('user/create/', views.LineUserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', views.LineUserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.LineUserDeleteView.as_view(), name='user_delete'),
]