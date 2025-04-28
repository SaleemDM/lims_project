from django.db import models

class methods(models.Model):
    method_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.method_name
