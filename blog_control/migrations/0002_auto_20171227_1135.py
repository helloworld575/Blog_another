# Generated by Django 2.0 on 2017-12-27 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlemodel',
            old_name='user',
            new_name='author',
        ),
    ]