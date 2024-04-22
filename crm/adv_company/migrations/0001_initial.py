# Generated by Django 5.0.3 on 2024-03-25 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvCompany",
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
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название компании"
                    ),
                ),
                (
                    "promotion_channel",
                    models.CharField(max_length=127, verbose_name="Канал продвижения"),
                ),
                (
                    "budget",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="Бюджет"
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.service",
                        verbose_name="Услуга",
                    ),
                ),
            ],
            options={
                "verbose_name": "Компания",
                "verbose_name_plural": "Компании",
            },
        ),
    ]
