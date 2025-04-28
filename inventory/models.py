from django.db import models

class inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name
