# Generated by Django 4.2.14 on 2024-07-31 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expensedb_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensedb',
            name='group',
        ),
    ]
