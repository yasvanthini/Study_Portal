# Generated by Django 4.2.16 on 2024-11-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NG_Support_Web", "0025_service_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="amenities",
            field=models.ManyToManyField(
                blank=True, related_name="services_list", to="NG_Support_Web.amenity"
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="contact_number",
            field=models.CharField(default="N/A", max_length=15),
        ),
        migrations.AddField(
            model_name="service",
            name="location",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
