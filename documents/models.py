from django.db import models

class documents(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    uploaded_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
