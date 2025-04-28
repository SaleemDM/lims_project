import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

expected_files = [
    "models.py", "views.py", "urls.py", "forms.py",
    "admin.py", "tests.py", "apps.py"
]

all_ok = True

for module in modules:
    print(f"\n📁 Checking module: {module}")
    for file in expected_files:
        path = os.path.join(module, file)
        if not os.path.exists(path):
            print(f"❌ Missing: {file}")
            all_ok = False
        else:
            print(f"✅ Found: {file}")

if all_ok:
    print("\n✅ All modules have the correct structure.")
else:
    print("\n⚠ Please fix the missing files.")
