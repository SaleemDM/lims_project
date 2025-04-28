from django.db import models

class stability(models.Model):
    batch_number = models.CharField(max_length=100)
    test_period = models.IntegerField(help_text="Duration in months")
    conditions = models.CharField(max_length=200)

    def __str__(self):
        return self.batch_number
