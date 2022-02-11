```
pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
cd ~
(drf) $ django-admin.py startproject tutorial .
(drf) $ python manage.py startapp snippets

tutorial/tutorial/settings.py 

INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets',
]












```