# Generated by Django 5.1.3 on 2024-11-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]