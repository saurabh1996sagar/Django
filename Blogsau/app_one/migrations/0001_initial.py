# Generated by Django 4.0.4 on 2022-06-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
    ]