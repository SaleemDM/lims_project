from django.db import models

class instruments(models.Model):
    instrument_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)

    def __str__(self):
        return self.instrument_name
