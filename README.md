<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-loadsql.svg?longCache=True)](https://pypi.org/project/django-loadsql/)
[![](https://img.shields.io/pypi/v/django-loadsql.svg?maxAge=3600)](https://pypi.org/project/django-loadsql/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-loadsql.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-loadsql.py/)

#### Installation
```bash
$ [sudo] pip install django-loadsql
```

#### Commands
command|`help`
-|-
`python manage.py loadsql` |load sql file(s)

#### Executable modules
usage|`__doc__`
-|-
`python -m django_loadsql path ...` |load sql file(s)

#### Examples
variant 1:

`settings.py`
```python
INSTALLED_APPS+= ["django_loadsql"]
```

```bash
$ find . -name '*.sql' | xargs python manage.py loadsql
```


variant 2:
```bash
export DJANGO_SETTINGS_MODULE=settings.dev
find . -name '*.sql' | xargs python -m django_loadsql
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>