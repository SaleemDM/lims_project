import os

apps = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

base_path = os.path.dirname(os.path.abspath(__file__))

for app in apps:
    models_path = os.path.join(base_path, app, "models.py")
    admin_path = os.path.join(base_path, app, "admin.py")

    # Skip if no models.py found
    if not os.path.exists(models_path):
        print(f"[SKIPPED] models.py not found in {app}")
        continue

    with open(models_path, "r") as f:
        lines = f.readlines()

    model_names = []
    for line in lines:
        if line.strip().startswith("class ") and "(models.Model)" in line:
            model_name = line.split("class ")[1].split("(")[0].strip()
            model_names.append(model_name)

    if not model_names:
        print(f"[INFO] No models found in {app}")
        continue

    with open(admin_path, "w") as f:
        f.write("from django.contrib import admin\n")
        f.write("from .models import " + ", ".join(model_names) + "\n\n")
        for model in model_names:
            f.write(f"admin.site.register({model})\n")

    print(f"[✅] admin.py generated for {app}")
