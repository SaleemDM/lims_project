import os

# Define folder and file structure excluding users/templates/users
template_structure = {
    "samples/templates/samples": ["sample_list.html", "sample_form.html"],
    "tests/templates/tests": ["test_list.html", "test_form.html"],
    "instruments/templates/instruments": ["instrument_list.html", "instrument_form.html"],
    "inventory/templates/inventory": ["inventory_list.html", "inventory_form.html"],
    "qc/templates/qc": ["qcrecord_list.html", "qcrecord_form.html"],
    "qa/templates/qa": ["qareport_list.html", "qareport_form.html"],
    "production/templates/production": ["productionbatch_list.html", "productionbatch_form.html"],
    "warehouse/templates/warehouse": ["warehouseitem_list.html", "warehouseitem_form.html"],
    "complaints/templates/complaints": ["complaint_list.html", "complaint_form.html"],
    "regulatory/templates/regulatory": ["regulatorysubmission_list.html", "regulatorysubmission_form.html"],
    "reports/templates/reports": ["report_list.html", "report_form.html"],
}

# Create folders and files
for folder, files in template_structure.items():
    os.makedirs(folder, exist_ok=True)
    for file_name in files:
        file_path = os.path.join(folder, file_name)
        with open(file_path, 'w') as f:
            f.write(f"<h1>{file_name}</h1>\n<p>Template for {file_name}</p>")
print("✅ All template files created (excluding users)!")
