import os

apps = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

base_path = os.path.dirname(os.path.abspath(__file__))

for app in apps:
    models_path = os.path.join(base_path, app, "models.py")
    model_class_name = app.capitalize()[:-1] if app.endswith('s') else app.capitalize()
    model_class_name += "Model"

    if not os.path.exists(models_path):
        with open(models_path, "w") as f:
            f.write("from django.db import models\n\n")
            f.write(f"class {model_class_name}(models.Model):\n")
            f.write("    name = models.CharField(max_length=100)\n\n")
            f.write("    def __str__(self):\n")
            f.write("        return self.name\n")
        print(f"[CREATED] models.py for {app} with {model_class_name}")
    else:
        print(f"[SKIPPED] models.py already exists in {app}")
