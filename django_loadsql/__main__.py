#!/usr/bin/env python
"""load sql file(s)"""
# -*- coding: utf-8 -*-
import click
import django
from django.db import connection

"""
export DJANGO_SETTINGS_MODULE=settings.dev
find . -name '*.sql' | xargs python -m django_loadsql
"""

MODULE_NAME = "django_loadsql"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME

def print_output(cursor):
    try:
        for row in cursor.fetchall():
            if row:
                print('|'.join(row))
    except:
        pass

@click.command()
@click.argument('paths',nargs=-1)
def _cli(paths):
    django.setup()
    cursor = connection.cursor()
    for path in paths:
        sql = open(path).read()
        cursor.execute(sql)
        print_output(cursor)

if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
