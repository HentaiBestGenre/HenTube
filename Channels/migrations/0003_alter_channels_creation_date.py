# Generated by Django 4.1 on 2022-09-18 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Channels', '0002_alter_channels_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channels',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 18, 15, 50, 498931, tzinfo=datetime.timezone.utc), verbose_name='creation date'),
        ),
    ]
