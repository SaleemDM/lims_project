from django.db import models

class tests(models.Model):
    test_name = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    result = models.TextField()

    def __str__(self):
        return self.test_name
