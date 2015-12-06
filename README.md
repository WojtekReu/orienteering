# orienteering
System for organizing sports competitions

====================
Project installation
====================

Create virtual environment in directory venv and using python in 3 version:

    virtualenv -p python3 venv

Activate environment:

    . venv/bin/activate

Install django-cms installer with dependiences:

    pip install djangocms-installer

Check:

    pip freeze

argparse==1.4.0
dj-database-url==0.3.0
djangocms-installer==0.8.3
pytz==2015.7
six==1.10.0
tzlocal==1.2

Create directory orient and go into:

    mkdir orient

    cd orient

In directory orient run django cms installer:

    djangocms -p . orient

Create migrations:

    ./manage.py makemigrations cup

    ./manage.py migrate cup

    ./manage.py makemigrations cup_plugin

    ./manage.py migrate cup_plugin

