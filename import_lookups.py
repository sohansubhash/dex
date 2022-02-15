import pandas as pd
from django.core.management import BaseCommand
from species.models import Types
from species.models import Shapes
from species.models import Colors
from species.models import Habitats

class Command(BaseCommand):
    help = 'Load lookup csv files into the database'

    def handle(self, *args, **kwargs):
        types=pd.read_csv('../data/lookup/types.csv',sep=',')
        colors=pd.read_csv('../data/lookup/colors.csv',sep=',')
        shapes=pd.read_csv('../data/lookup/shapes.csv',sep=',')
        habitats=pd.read_csv('../data/lookup/habitats.csv',sep=',')

        row_iter = types.iterrows()
        objs = [
            Types(
                type_id = row['type_id'],
                type_name = row['type_name'],
            )
            for index, row in row_iter
        ]

        Types.objects.bulk_create(objs)

        row_iter = colors.iterrows()
        objs = [
            Colors(
                colors_id = row['colors_id'],
                colors_name = row['colors_name'],
            )
            for index, row in row_iter
        ]

        Colors.objects.bulk_create(objs)

        row_iter = shapes.iterrows()
        objs = [
            Shapes(
                shapes_id = row['shapes_id'],
                shapes_name = row['shapes_name'],
            )
            for index, row in row_iter
        ]

        Shapes.objects.bulk_create(objs)


        row_iter = habitats.iterrows()
        objs = [
            Types(
                habitats_id = row['habitats_id'],
                habitats_name = row['habitats_name'],
            )
            for index, row in row_iter
        ]

        Habitats.objects.bulk_create(objs)
