# Generated by Django 4.2.16 on 2024-10-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NG_Support_Web", "0012_listing_description_listing_facebook_url_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="thumbnails/"),
        ),
    ]
