# Generated by Django 2.2.4 on 2019-08-13 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devbook', '0002_auto_20190813_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 13, 15, 13, 10, 63365)),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 13, 15, 13, 10, 66114)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 13, 15, 13, 10, 62895)),
        ),
    ]
