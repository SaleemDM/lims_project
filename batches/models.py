from django.db import models

class batches(models.Model):
    batch_number = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=200)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.batch_number
