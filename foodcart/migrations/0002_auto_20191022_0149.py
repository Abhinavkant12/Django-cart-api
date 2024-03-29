# Generated by Django 2.2.6 on 2019-10-21 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 1, 49, 4, 890067), verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='cuisinetype',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 1, 49, 4, 889066), verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='mealtype',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 1, 49, 4, 887031), verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 1, 49, 4, 889066), verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='menurating',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 1, 49, 4, 890067), verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='state',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 1, 49, 4, 888062), verbose_name='Creation Date'),
        ),
    ]
