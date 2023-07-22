from django.urls import path
from . import views

# All URL pathways within the User App
urlpatterns = [
    path('', views.user_view, name="user_view"),
    path('change/password/', views.user_password_change, name="user_password_change"),
    path('change/details/', views.user_details_change, name="user_details_change"),
    path('delete/', views.user_delete, name="user_delete"),
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('logout/', views.user_logout, name="logout"),
]
