# Generated by Django 2.2 on 2019-04-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190405_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.CharField(default='Name | Era', max_length=50),
            preserve_default=False,
        ),
    ]
