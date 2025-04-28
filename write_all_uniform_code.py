import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

boilerplate = {
    "models.py": "from django.db import models\n\n# Create your models here.\n",
    "admin.py": "from django.contrib import admin\nfrom .models import *\n\n# Register your models here.\n",
    "forms.py": "from django import forms\nfrom .models import *\n\n# Define your forms here.\n",
    "urls.py": (
        "from django.urls import path\n"
        "from . import views\n\n"
        "app_name = '{module}'\n\n"
        "urlpatterns = [\n"
        "    path('', views.index, name='index'),\n"
        "]\n"
    ),
    "views.py": (
        "from django.shortcuts import render\n\n"
        "def index(request):\n"
        "    return render(request, '{module}/index.html')\n"
    ),
    "tests.py": "from django.test import TestCase\n\n# Create your tests here.\n",
    "__init__.py": ""
}

for module in modules:
    for filename, content in boilerplate.items():
        file_path = os.path.join(module, filename)
        with open(file_path, 'w') as f:
            f.write(content.replace("{module}", module))

print("✅ Boilerplate code written to all module files.")
