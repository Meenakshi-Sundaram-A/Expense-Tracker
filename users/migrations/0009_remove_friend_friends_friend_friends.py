# Generated by Django 4.2.14 on 2024-08-07 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_remove_friend_friends_friend_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friends',
        ),
        migrations.AddField(
            model_name='friend',
            name='friends',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
