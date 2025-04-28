import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "batches", "results", "reports", "documents"
]

standard_files = [
    "__init__.py", "admin.py", "apps.py", "models.py",
    "tests.py", "views.py", "urls.py", "forms.py"
]

for module in modules:
    if not os.path.exists(module):
        os.makedirs(module)
        print(f"📁 Created folder: {module}")
    for file_name in standard_files:
        file_path = os.path.join(module, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")
            print(f"✅ Created: {file_path}")
        else:
            print(f"✔️ Exists: {file_path}")
