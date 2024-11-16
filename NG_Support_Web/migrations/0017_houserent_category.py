# Generated by Django 4.2.16 on 2024-11-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("NG_Support_Web", "0016_houserent"),
    ]

    operations = [
        migrations.AddField(
            model_name="houserent",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="house_rents",
                to="NG_Support_Web.category",
            ),
        ),
    ]
