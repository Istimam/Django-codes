# Generated by Django 5.0.6 on 2024-05-14 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_task_category_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='task',
            new_name='categories',
        ),
    ]