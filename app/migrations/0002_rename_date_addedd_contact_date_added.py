# Generated by Django 4.2.9 on 2024-01-11 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date_addedd',
            new_name='date_added',
        ),
    ]