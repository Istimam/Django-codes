# Generated by Django 5.0.6 on 2024-05-14 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_rename_task_category_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categories',
        ),
    ]