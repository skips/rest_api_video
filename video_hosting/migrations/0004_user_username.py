# Generated by Django 4.0.4 on 2022-05-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0003_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
