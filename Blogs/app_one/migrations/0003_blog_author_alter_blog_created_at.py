# Generated by Django 4.0.4 on 2022-05-29 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='Admin', max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 1, 18, 9, 175031)),
        ),
    ]
