# Generated by Django 4.0.3 on 2022-05-24 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='type',
            new_name='plant_type',
        ),
    ]
