# Generated by Django 4.2.2 on 2023-06-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_alter_create_event_remaining_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_event',
            name='end_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='start_Date',
            field=models.DateField(),
        ),
    ]