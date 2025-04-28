import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

required_files = [
    "__init__.py", "models.py", "views.py", "urls.py",
    "forms.py", "admin.py", "tests.py", "apps.py"
]

for module in modules:
    if not os.path.exists(module):
        os.makedirs(module)
        print(f"📁 Created folder: {module}")
    for file in required_files:
        path = os.path.join(module, file)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(f"# {file} for {module} module\n")
            print(f"✅ Created: {path}")
        else:
            print(f"🔹 Exists: {path}")
