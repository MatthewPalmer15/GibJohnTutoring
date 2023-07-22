# Generated by Django 3.2.12 on 2022-03-09 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('content', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=128)),
                ('option_1', models.CharField(max_length=128)),
                ('option_2', models.CharField(max_length=128)),
                ('option_3', models.CharField(max_length=128, null=True)),
                ('option_4', models.CharField(max_length=128, null=True)),
                ('answer', models.CharField(max_length=128)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('award_id', models.AutoField(primary_key=True, serialize=False)),
                ('trophy', models.CharField(max_length=32)),
                ('user_marks', models.PositiveIntegerField()),
                ('total_marks', models.PositiveIntegerField()),
                ('percentage', models.PositiveIntegerField()),
                ('completion_date', models.DateTimeField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]