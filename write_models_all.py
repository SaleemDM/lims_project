# write_models_all.py
import os

models_code = {
    "users": '''
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('lab_user', 'Lab User'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='lab_user')
''',

    "samples": '''
from django.db import models

class Sample(models.Model):
    sample_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    sample_type = models.CharField(max_length=100)
    collected_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.sample_id
''',

    "tests": '''
from django.db import models
from samples.models import Sample

class Test(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    result = models.CharField(max_length=100)
    test_date = models.DateField()

    def __str__(self):
        return f"{self.test_name} - {self.sample.sample_id}"
''',

    "instruments": '''
from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=200)
    model_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    calibration_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
''',

    "inventory": '''
from django.db import models

class InventoryItem(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    received_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.item_name
''',

    "methods": '''
from django.db import models

class Method(models.Model):
    method_name = models.CharField(max_length=200)
    description = models.TextField()
    version = models.CharField(max_length=50)
    effective_date = models.DateField()

    def __str__(self):
        return self.method_name
''',

    "training": '''
from django.db import models
from users.models import CustomUser

class TrainingRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    training_name = models.CharField(max_length=200)
    completion_date = models.DateField()
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f"{self.training_name} - {self.user.username}"
''',

    "documents": '''
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
''',

    "deviations": '''
from django.db import models

class Deviation(models.Model):
    deviation_id = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date_reported = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.deviation_id
''',

    "audit_trail": '''
from django.db import models
from users.models import CustomUser

class AuditTrail(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    module = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.action}"
''',

    "reports": '''
from django.db import models

class Report(models.Model):
    report_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    generated_by = models.CharField(max_length=100)
    file = models.FileField(upload_to='reports/')

    def __str__(self):
        return self.report_name
''',

    "settings_module": '''
from django.db import models

class LabSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key
'''
}

for app, code in models_code.items():
    file_path = os.path.join(app, 'models.py')
    with open(file_path, 'w') as f:
        f.write(code.strip())
    print(f"✅ {file_path} written.")
