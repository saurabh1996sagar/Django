# Generated by Django 4.0.5 on 2022-07-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_one', '0002_remove_room_room_name_room_rooom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='rooom_id',
            field=models.IntegerField(default='N/A'),
        ),
    ]
