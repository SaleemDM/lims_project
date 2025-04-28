import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "batches", "results", "reports", "documents"
]

for module in modules:
    class_name = module.capitalize() + "Config"
    content = f"""from django.apps import AppConfig

class {class_name}(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{module}'
"""
    file_path = os.path.join(module, "apps.py")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ apps.py written for {module}")
