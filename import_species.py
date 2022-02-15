import pandas as pd
from django.core.management import BaseCommand
from species.models import Species


df=pd.read_csv('../data/pokemon/pokemon.csv',sep=';')

class Command(BaseCommand):
    help = 'Load pokemon csv file into the database'
    def handle(self, *args, **kwargs):
        row_iter = df.iterrows()
        objs = [
            Species(
                dex_id = row['dex_id'],
                name = row['name'],
                genus = row['genus'],
                type_one = row['type_one'],
                type_two = row['type_two'],
                height = row['height'],
                weight = row['weight'],
                color_id = row['color_id'],
                shape_id = row['shape_id'],
                evolves_from_dex_id = row['evolves_from_dex_id'],
                evolution_chain_id = row['evolution_chain_id'],
                capture_rate = row['capture_rate'],
                habitat_id = row['habitat_id'],
                base_experience = row['base_experience'],
                growth_rate_id = row['growth_rate_id'],
                is_legendary = row['is_legendary'],
                is_mythical = row['is_mythical'],
                hp = row['hp'],
                attack = row['attack'],
                defense = row['defense'],
                special = row['special'],
                speed = row['speed']
            )
            for index, row in row_iter
        ]

        Species.objects.bulk_create(objs)
