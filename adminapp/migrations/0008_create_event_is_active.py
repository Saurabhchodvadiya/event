# Generated by Django 4.2.2 on 2023-06-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_create_event_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_event',
            name='is_active',
            field=models.BooleanField(default=1),
        ),
    ]