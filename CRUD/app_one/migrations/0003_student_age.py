# Generated by Django 4.0.4 on 2022-05-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default='10'),
        ),
    ]
