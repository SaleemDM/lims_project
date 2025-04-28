from django.db import models

class samples(models.Model):
    sample_id = models.CharField(max_length=50)
    description = models.TextField()
    collected_on = models.DateField()

    def __str__(self):
        return self.sample_id
