import os

url_patterns = {
    "samples": """from django.urls import path
from samples.views import SampleListView, SampleCreateView

urlpatterns = [
    path('', SampleListView.as_view(), name='sample_list'),
    path('add/', SampleCreateView.as_view(), name='sample_add'),
]
""",
    "tests": """from django.urls import path
from tests.views import TestListView, TestCreateView

urlpatterns = [
    path('', TestListView.as_view(), name='test_list'),
    path('add/', TestCreateView.as_view(), name='test_add'),
]
""",
    "instruments": """from django.urls import path
from instruments.views import InstrumentListView, InstrumentCreateView

urlpatterns = [
    path('', InstrumentListView.as_view(), name='instrument_list'),
    path('add/', InstrumentCreateView.as_view(), name='instrument_add'),
]
""",
    "inventory": """from django.urls import path
from inventory.views import InventoryListView, InventoryCreateView

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory_list'),
    path('add/', InventoryCreateView.as_view(), name='inventory_add'),
]
""",
    "qc": """from django.urls import path
from qc.views import QCRecordListView, QCRecordCreateView

urlpatterns = [
    path('', QCRecordListView.as_view(), name='qcrecord_list'),
    path('add/', QCRecordCreateView.as_view(), name='qcrecord_add'),
]
""",
    "qa": """from django.urls import path
from qa.views import QAReportListView, QAReportCreateView

urlpatterns = [
    path('', QAReportListView.as_view(), name='qareport_list'),
    path('add/', QAReportCreateView.as_view(), name='qareport_add'),
]
""",
    "production": """from django.urls import path
from production.views import ProductionBatchListView, ProductionBatchCreateView

urlpatterns = [
    path('', ProductionBatchListView.as_view(), name='productionbatch_list'),
    path('add/', ProductionBatchCreateView.as_view(), name='productionbatch_add'),
]
""",
    "warehouse": """from django.urls import path
from warehouse.views import WarehouseItemListView, WarehouseItemCreateView

urlpatterns = [
    path('', WarehouseItemListView.as_view(), name='warehouseitem_list'),
    path('add/', WarehouseItemCreateView.as_view(), name='warehouseitem_add'),
]
""",
    "complaints": """from django.urls import path
from complaints.views import ComplaintListView, ComplaintCreateView

urlpatterns = [
    path('', ComplaintListView.as_view(), name='complaint_list'),
    path('add/', ComplaintCreateView.as_view(), name='complaint_add'),
]
""",
    "regulatory": """from django.urls import path
from regulatory.views import RegulatorySubmissionListView, RegulatorySubmissionCreateView

urlpatterns = [
    path('', RegulatorySubmissionListView.as_view(), name='regulatorysubmission_list'),
    path('add/', RegulatorySubmissionCreateView.as_view(), name='regulatorysubmission_add'),
]
""",
    "reports": """from django.urls import path
from reports.views import ReportListView, ReportCreateView

urlpatterns = [
    path('', ReportListView.as_view(), name='report_list'),
    path('add/', ReportCreateView.as_view(), name='report_add'),
]
"""
}

# Create each urls.py file
for app, code in url_patterns.items():
    os.makedirs(app, exist_ok=True)
    file_path = os.path.join(app, "urls.py")
    with open(file_path, "w") as f:
        f.write(code)

print("✅ All urls.py files have been created in their respective app folders.")
