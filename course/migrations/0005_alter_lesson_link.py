# Generated by Django 5.0.6 on 2024-07-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.TextField(blank=True, null=True, verbose_name='Lesson link'),
        ),
    ]
