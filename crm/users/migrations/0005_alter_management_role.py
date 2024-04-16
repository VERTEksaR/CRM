# Generated by Django 5.0.3 on 2024-04-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_management_user_alter_management_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='role',
            field=models.CharField(choices=[('Менеджер', 'Менеджер'), ('Маркетолог', 'Маркетолог'), ('Администратор', 'Администратор'), ('Оператор', 'Оператор')], max_length=63, verbose_name='Роль'),
        ),
    ]