# Generated by Django 4.2.16 on 2024-11-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NG_Support_Web", "0032_service_city_service_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="houserent",
            name="contact_number",
            field=models.CharField(max_length=30),
        ),
    ]