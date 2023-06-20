# Generated by Django 4.2.2 on 2023-06-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('created_date', models.DateField(blank=True, max_length=20)),
                ('updated_date', models.DateField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=1)),
                ('is_admin', models.BooleanField(default=0)),
            ],
        ),
    ]