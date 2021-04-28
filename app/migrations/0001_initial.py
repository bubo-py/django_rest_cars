# Generated by Django 3.2 on 2021-04-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make', models.CharField(max_length=40)),
                ('car_model', models.CharField(max_length=40)),
                ('car_year', models.CharField(max_length=4)),
                ('car_vin', models.CharField(max_length=20)),
            ],
        ),
    ]