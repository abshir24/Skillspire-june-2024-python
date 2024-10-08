# Generated by Django 4.2.16 on 2024-09-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djA7", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("height", models.FloatField()),
                ("weight", models.FloatField()),
                ("dietary_preference", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
