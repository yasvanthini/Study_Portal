# Generated by Django 4.2.16 on 2024-10-29 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "NG_Support_Web",
            "0010_alter_listing_city_alter_listing_contact_number_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
    ]