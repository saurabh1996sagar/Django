# Generated by Django 4.0.5 on 2022-07-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_one', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_name',
        ),
        migrations.AddField(
            model_name='room',
            name='rooom_id',
            field=models.IntegerField(default='NULL'),
        ),
    ]
