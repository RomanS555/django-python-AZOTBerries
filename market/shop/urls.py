
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cards/', views.cards),
    path('action_click/', views.action_click, name='action_click'),
    path('action_delete/', views.action_click, name='action_delete'),
]
