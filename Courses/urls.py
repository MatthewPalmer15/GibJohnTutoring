from django.urls import path
from . import views

# All URLs that are part of the Course App
urlpatterns = [
    path('', views.view_courses, name="view_courses"),
    path('<int:id>/overview', views.course_overview, name="course_overview"),
    path('<int:id>/content', views.course_content, name="course_content"),
    path('<int:id>/assessment', views.course_questions, name="course_questions"),
]
