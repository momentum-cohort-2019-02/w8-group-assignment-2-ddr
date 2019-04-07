# Generated by Django 2.2 on 2019-04-07 16:23

from django.db import migrations
from django.conf import settings
from django.utils.text import slugify

import os.path
import csv

def load_cards(apps, schema_editor):
    """Read CSV file of comment data and add it to the posts"""
    Card = apps.get_model('core', 'Card')

    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'cards.csv')

    with open(datafile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name_era_card = Card(
                front = row['Name'],
                back = row['Era'],
                slug = slugify(row['Name'] + row['Era'])[:50],
                category = 'Name | Era',
            )
            name_era_card.save()

            if not (row['Image'] == 'None'):
                image_name_card = Card(
                    front = row['Name'],
                    back = row['Name'],
                    slug = slugify('image' + row['Name'])[:50],
                    category = 'Image | Name',
                    front_image_path = '/static/card_images/' + row['Name'] + '.jpg'
                )
                image_name_card.save()

            name_diet_card = Card(
                front = row['Name'],
                back = row['Diet'],
                slug = slugify(row['Name'] + row['Diet'])[:50],
                category = 'Name | Diet',
            )
            name_diet_card.save()

            name_type_card = Card(
                front = row['Name'],
                back = row['Type'],
                slug = slugify(row['Name'] + row['Type'])[:50],
                category = 'Name | Type',
            )
            name_type_card.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [migrations.RunPython(load_cards)
    ]