# Generated by Django 4.2.16 on 2024-11-06 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("NG_Support_Web", "0030_remove_service_amenity_service"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service",
            old_name="amenities",
            new_name="service_amenities",
        ),
    ]
