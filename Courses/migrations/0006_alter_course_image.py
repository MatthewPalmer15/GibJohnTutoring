# Generated by Django 3.2.12 on 2022-03-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0005_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/course'),
        ),
    ]
