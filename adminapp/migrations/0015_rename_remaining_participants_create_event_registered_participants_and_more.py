# Generated by Django 4.2.2 on 2023-06-20 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_create_event_remaining_participants_register_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create_event',
            old_name='remaining_participants',
            new_name='registered_participants',
        ),
        migrations.DeleteModel(
            name='register_event',
        ),
    ]
