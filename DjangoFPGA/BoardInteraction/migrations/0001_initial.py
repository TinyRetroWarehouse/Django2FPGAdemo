# Generated by Django 3.0.2 on 2020-01-22 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADCSensorReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(db_index=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ADCchannle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('ch', models.IntegerField()),
                ('readings', models.ManyToManyField(to='BoardInteraction.ADCSensorReading')),
            ],
        ),
    ]