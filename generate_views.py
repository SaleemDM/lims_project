import os

views_code = {
    "samples": """from django.views.generic import ListView, CreateView
from .models import Sample
from .forms import SampleForm

class SampleListView(ListView):
    model = Sample
    template_name = 'samples/sample_list.html'

class SampleCreateView(CreateView):
    model = Sample
    form_class = SampleForm
    template_name = 'samples/sample_form.html'
    success_url = '/samples/'
""",

    "tests": """from django.views.generic import ListView, CreateView
from .models import Test
from .forms import TestForm

class TestListView(ListView):
    model = Test
    template_name = 'tests/test_list.html'

class TestCreateView(CreateView):
    model = Test
    form_class = TestForm
    template_name = 'tests/test_form.html'
    success_url = '/tests/'
""",

    "instruments": """from django.views.generic import ListView, CreateView
from .models import Instrument
from .forms import InstrumentForm

class InstrumentListView(ListView):
    model = Instrument
    template_name = 'instruments/instrument_list.html'

class InstrumentCreateView(CreateView):
    model = Instrument
    form_class = InstrumentForm
    template_name = 'instruments/instrument_form.html'
    success_url = '/instruments/'
""",

    "inventory": """from django.views.generic import ListView, CreateView
from .models import InventoryItem
from .forms import InventoryForm

class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'

class InventoryCreateView(CreateView):
    model = InventoryItem
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = '/inventory/'
""",

    "qc": """from django.views.generic import ListView, CreateView
from .models import QCRecord
from .forms import QCRecordForm

class QCRecordListView(ListView):
    model = QCRecord
    template_name = 'qc/qcrecord_list.html'

class QCRecordCreateView(CreateView):
    model = QCRecord
    form_class = QCRecordForm
    template_name = 'qc/qcrecord_form.html'
    success_url = '/qc/'
""",

    "qa": """from django.views.generic import ListView, CreateView
from .models import QAReport
from .forms import QAReportForm

class QAReportListView(ListView):
    model = QAReport
    template_name = 'qa/qareport_list.html'

class QAReportCreateView(CreateView):
    model = QAReport
    form_class = QAReportForm
    template_name = 'qa/qareport_form.html'
    success_url = '/qa/'
""",

    "production": """from django.views.generic import ListView, CreateView
from .models import ProductionBatch
from .forms import ProductionBatchForm

class ProductionBatchListView(ListView):
    model = ProductionBatch
    template_name = 'production/productionbatch_list.html'

class ProductionBatchCreateView(CreateView):
    model = ProductionBatch
    form_class = ProductionBatchForm
    template_name = 'production/productionbatch_form.html'
    success_url = '/production/'
""",

    "warehouse": """from django.views.generic import ListView, CreateView
from .models import WarehouseItem
from .forms import WarehouseItemForm

class WarehouseItemListView(ListView):
    model = WarehouseItem
    template_name = 'warehouse/warehouseitem_list.html'

class WarehouseItemCreateView(CreateView):
    model = WarehouseItem
    form_class = WarehouseItemForm
    template_name = 'warehouse/warehouseitem_form.html'
    success_url = '/warehouse/'
""",

    "complaints": """from django.views.generic import ListView, CreateView
from .models import Complaint
from .forms import ComplaintForm

class ComplaintListView(ListView):
    model = Complaint
    template_name = 'complaints/complaint_list.html'

class ComplaintCreateView(CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'complaints/complaint_form.html'
    success_url = '/complaints/'
""",

    "regulatory": """from django.views.generic import ListView, CreateView
from .models import RegulatorySubmission
from .forms import RegulatorySubmissionForm

class RegulatorySubmissionListView(ListView):
    model = RegulatorySubmission
    template_name = 'regulatory/regulatorysubmission_list.html'

class RegulatorySubmissionCreateView(CreateView):
    model = RegulatorySubmission
    form_class = RegulatorySubmissionForm
    template_name = 'regulatory/regulatorysubmission_form.html'
    success_url = '/regulatory/'
""",

    "reports": """from django.views.generic import ListView, CreateView
from .models import Report
from .forms import ReportForm

class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'
    success_url = '/reports/'
"""
}

# Create views.py in each app
for app, content in views_code.items():
    path = os.path.join(app, 'views.py')
    os.makedirs(app, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

print("✅ All views.py files created successfully!")
