# Generated by Django 4.2.2 on 2023-06-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_create_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_event',
            name='end_Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='start_Date',
            field=models.DateTimeField(),
        ),
    ]
