# Generated by Django 3.0.4 on 2020-03-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet_help", "0002_add_lat_lng_fields_to_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="user", name="email_verified", field=models.BooleanField(default=True),
        ),
    ]
