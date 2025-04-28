import os

apps = [
    "tests", "instruments", "batches", "products",
    "specifications", "analysts", "results",
    "reports", "audit_trails", "attachments"
]

base_path = os.getcwd()

# Template content for standard Django files
init_file = ""
admin_file = "from django.contrib import admin\n"
apps_file = """from django.apps import AppConfig

class {classname}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{appname}'
"""
models_file = "from django.db import models\n"
views_file = "from django.shortcuts import render\n"
forms_file = "from django import forms\n"
urls_file = """from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='{appname}_index'),
]
"""
tests_file = """from django.test import TestCase

# Create your tests here.
"""

for app in apps:
    app_path = os.path.join(base_path, app)
    os.makedirs(app_path, exist_ok=True)

    # Create standard files
    files = {
        '__init__.py': init_file,
        'admin.py': admin_file,
        'apps.py': apps_file.format(classname=app.capitalize(), appname=app),
        'models.py': models_file,
        'views.py': views_file,
        'forms.py': forms_file,
        'urls.py': urls_file.replace('{appname}', app),
        'tests.py': tests_file
    }

    for filename, content in files.items():
        with open(os.path.join(app_path, filename), 'w') as f:
            f.write(content)

    # Create templates folder for the app
    templates_path = os.path.join(app_path, 'templates', app)
    os.makedirs(templates_path, exist_ok=True)

print("✅ All 10 apps generated (excluding users and samples).")
