import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

for module in modules:
    file_path = os.path.join(module, "forms.py")
    os.makedirs(module, exist_ok=True)

    content = """from django import forms

# Define your forms here.
"""

    with open(file_path, "w") as f:
        f.write(content)

print("✅ All forms.py files generated.")
