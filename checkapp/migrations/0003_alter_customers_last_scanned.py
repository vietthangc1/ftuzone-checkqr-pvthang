# Generated by Django 3.2.5 on 2021-10-14 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0002_alter_customers_yearofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='last_scanned',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
