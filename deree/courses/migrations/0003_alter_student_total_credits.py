# Generated by Django 4.0.3 on 2022-03-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_student_courses_remove_course_course_credits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='total_credits',
            field=models.IntegerField(default=0),
        ),
    ]
