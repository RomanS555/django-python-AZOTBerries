
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_page),
    path('registration/', views.registration),
    path('logout/', views.logout)
]
