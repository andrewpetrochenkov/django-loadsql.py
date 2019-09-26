from django.core.management.base import BaseCommand
from django.db import connection


"""
settings.py:
INSTALLED_APPS+= ["django_loadsql"]

find . -name '*.sql' | xargs python manage.py loadsql
"""

class Command(BaseCommand):
    help = 'load sql file(s)'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('args', nargs='+', help='paths')

    def handle(self, *args, **options):
        cursor = connection.cursor()
        for path in args:
            sql = open(path).read()
        cursor.execute(sql)
