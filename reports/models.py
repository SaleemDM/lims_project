from django.db import models

class reports(models.Model):
    report_name = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.report_name
