# Generated by Django 4.1.13 on 2024-06-16 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='party_of_speech',
            new_name='part_of_speech',
        ),
    ]
