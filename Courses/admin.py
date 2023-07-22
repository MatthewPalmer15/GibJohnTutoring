from django.contrib import admin
from .models import Course, Question, Award

# Registers all Models onto the Admin Site
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Award)