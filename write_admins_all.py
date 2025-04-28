import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

for module in modules:
    file_path = os.path.join(module, "admin.py")
    os.makedirs(module, exist_ok=True)

    content = """from django.contrib import admin

# Register your models here.
"""

    with open(file_path, "w") as f:
        f.write(content)

print("✅ All admin.py files generated.")
