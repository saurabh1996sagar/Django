# Generated by Django 4.0.4 on 2022-05-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=25)),
                ('address', models.TextField()),
            ],
        ),
    ]