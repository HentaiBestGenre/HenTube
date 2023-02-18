# Generated by Django 4.1 on 2022-09-18 18:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Channels', '0003_alter_channels_creation_date'),
        ('Videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='reactions',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Channels.channels'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Videos.videos'),
        ),
        migrations.AlterField(
            model_name='reactions',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='Channels.channels'),
        ),
        migrations.AlterField(
            model_name='reactions',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='Videos.videos'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 18, 15, 50, 500931, tzinfo=datetime.timezone.utc), verbose_name='publication date'),
        ),
    ]
