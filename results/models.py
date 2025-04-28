from django.db import models

class results(models.Model):
    sample_id = models.CharField(max_length=100)
    test_name = models.CharField(max_length=200)
    result_value = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    date_tested = models.DateField()

    def __str__(self):
        return f"{self.sample_id} - {self.test_name}"
