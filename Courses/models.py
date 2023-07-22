from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Database Model for the Course, which is used for the different topics that GibJohn Tutoring offers
class Course(models.Model):
    course_id           = models.AutoField(primary_key=True)
    title               = models.CharField(max_length=64, null=False)
    description         = models.TextField(max_length=512, null=False)
    content             = RichTextField(max_length=4096, null=False)
    image               = models.ImageField(upload_to="static/images/course", null=True)

    def __str__(self):
        return f"{self.title}"

# Database Model for the Award, which is used to keep a record of the Awards earned
class Award(models.Model):
    award_id            = models.AutoField(primary_key=True)
    course_id           = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    user_id             = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    trophy              = models.CharField(max_length=32, null=False)
    user_marks          = models.PositiveIntegerField(null=False)
    total_marks         = models.PositiveIntegerField(null=False)
    percentage          = models.PositiveIntegerField(null=False)
    completion_date     = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.user_id.username} | {self.course_id.title} | {self.trophy} | {self.completion_date}"

# Database Model for the Questions, which is used within the assessnebt of a course
class Question(models.Model):
    question_id         = models.AutoField(primary_key=True)
    course_id           = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    question            = models.CharField(max_length=128, null=False)
    option_1            = models.CharField(max_length=128, null=False)
    option_2            = models.CharField(max_length=128, null=False)
    option_3            = models.CharField(max_length=128, null=True)
    option_4            = models.CharField(max_length=128, null=True)
    answer              = models.CharField(max_length=128, null=False)

    def __str__(self):
        return f"{self.course_id.title} | {self.question}"
