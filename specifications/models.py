from django.db import models

class specifications(models.Model):
    specification_name = models.CharField(max_length=100)
    parameter = models.CharField(max_length=100)
    limit = models.CharField(max_length=50)

    def __str__(self):
        return self.specification_name
