# Generated by Django 4.2.2 on 2023-06-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_alter_create_event_ending_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_event',
            name='deleted_By_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='create_event',
            name='updated_By_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
