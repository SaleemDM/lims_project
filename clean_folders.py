import os
import shutil

# List of required 12 modules
allowed_modules = {
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
}

# Get all folders in current directory
all_items = os.listdir(".")

# Loop and delete folders not in the allowed list
for item in all_items:
    if os.path.isdir(item) and item not in allowed_modules and not item.startswith('.'):
        try:
            shutil.rmtree(item)
            print(f"🗑️ Deleted folder: {item}")
        except Exception as e:
            print(f"❌ Error deleting {item}: {e}")
