import os

modules = [
    "users", "samples", "tests", "instruments", "inventory", "methods",
    "specifications", "stability", "calibration", "environmental", "microbiology", "deviations"
]

base_dir = os.path.join("templates")

for module in modules:
    module_template_dir = os.path.join(base_dir, module)
    os.makedirs(module_template_dir, exist_ok=True)
    file_path = os.path.join(module_template_dir, "index.html")

    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{module.title()} Module</title>
</head>
<body>
    <h1>Welcome to the {module.title()} Module</h1>
    <p>This is the index page for the <strong>{module}</strong> module.</p>
</body>
</html>
"""
    with open(file_path, 'w') as f:
        f.write(content)

print("✅ All index.html templates generated for each module.")
