# Generated by Django 4.2.14 on 2024-07-24 06:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_alter_friendsgroup_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendsgroup',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='group', to=settings.AUTH_USER_MODEL),
        ),
    ]
