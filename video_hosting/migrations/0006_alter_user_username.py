# Generated by Django 4.0.4 on 2022-05-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
