# Generated by Django 5.0.3 on 2024-03-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0001_initial"),
        ("adv_company", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="advcompany",
            name="service",
        ),
        migrations.AddField(
            model_name="advcompany",
            name="service",
            field=models.ManyToManyField(to="service.service", verbose_name="Услуга"),
        ),
    ]
