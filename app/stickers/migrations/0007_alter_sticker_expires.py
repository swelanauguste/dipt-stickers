# Generated by Django 5.1.3 on 2024-11-27 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0006_alter_sticker_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='expires',
            field=models.DateField(default=datetime.datetime(2025, 11, 27, 15, 18, 52, 907258, tzinfo=datetime.timezone.utc), help_text='MM/DD/YYYY', null=True),
        ),
    ]
