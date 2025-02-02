# Generated by Django 4.2.14 on 2024-08-02 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_friendsgroup_creator'),
        ('expense', '0005_expensesplit'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensedb',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='users.friendsgroup'),
        ),
    ]
