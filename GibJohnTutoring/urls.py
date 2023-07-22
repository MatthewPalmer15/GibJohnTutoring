from django.contrib import admin
from django.urls import path, include
from . import views

# All URLs that are part of the GibJohn Tutoring Web Application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Users.urls')),
    path('course/', include('Courses.urls')),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('privacy-policy/', views.policy, name="policy"),
]
