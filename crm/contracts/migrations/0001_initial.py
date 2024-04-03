# Generated by Django 5.0.3 on 2024-04-03 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название контракта')),
                ('file', models.FileField(upload_to='contracts/documents/', verbose_name='Файл')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Дата заключения')),
                ('period', models.CharField(max_length=127, verbose_name='Период действия контракта')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Контракт',
                'verbose_name_plural': 'Контракты',
            },
        ),
    ]
