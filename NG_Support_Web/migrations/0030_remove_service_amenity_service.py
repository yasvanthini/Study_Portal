# Generated by Django 4.2.16 on 2024-11-06 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("NG_Support_Web", "0029_alter_service_amenities"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service_amenity",
            name="service",
        ),
    ]
