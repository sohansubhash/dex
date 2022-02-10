```
pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
cd ~
django-admin.py startproject tutorial
cd tutorial
python manage.py startapp snippets

tutorial/tutorial/settings.py 

INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets',
]












```