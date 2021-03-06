# Generated by Django 3.0.4 on 2020-03-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet_help", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="current_address_lat",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="animal",
            name="current_address_lng",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="address_lat",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="address_lng",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="helprequest",
            name="animals",
            field=models.ManyToManyField(related_name="requests", to="pet_help.Animal"),
        ),
    ]
