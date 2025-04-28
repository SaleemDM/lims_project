import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

for module in modules:
    file_path = os.path.join(module, "tests.py")
    os.makedirs(module, exist_ok=True)

    content = """from django.test import TestCase

# Create your tests here.
"""

    with open(file_path, "w") as f:
        f.write(content)

print("✅ All tests.py files generated.")
