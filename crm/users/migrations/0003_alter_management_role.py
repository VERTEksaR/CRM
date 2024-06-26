# Generated by Django 5.0.3 on 2024-04-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_management"),
    ]

    operations = [
        migrations.AlterField(
            model_name="management",
            name="role",
            field=models.CharField(
                choices=[
                    ("Маркетолог", "Маркетолог"),
                    ("Администратор", "Администратор"),
                    ("Оператор", "Оператор"),
                    ("Менеджер", "Менеджер"),
                ],
                max_length=63,
            ),
        ),
    ]
