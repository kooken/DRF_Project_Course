# Generated by Django 5.0.6 on 2024-07-13 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_lesson_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='title',
            new_name='course',
        ),
    ]