# Generated by Django 5.0.3 on 2024-04-03 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_alter_contract_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='period',
        ),
        migrations.AddField(
            model_name='contract',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 4, 10, 18, 30, 137844, tzinfo=datetime.timezone.utc), verbose_name='Дата расторжения'),
        ),
    ]
