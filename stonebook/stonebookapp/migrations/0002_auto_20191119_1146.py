# Generated by Django 2.2.7 on 2019-11-19 11:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stonebookapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='AppGroup',

        ),


    ]
