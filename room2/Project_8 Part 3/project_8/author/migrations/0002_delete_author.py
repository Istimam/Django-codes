# Generated by Django 5.0.6 on 2024-05-23 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('posts', '0002_alter_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
