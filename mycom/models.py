from django.db import models

# Create your models here.
class blogs(models.Model):
    name = models.CharField(max_length= 30)
    gmail = models.CharField(max_length= 30)
    comments = models.CharField(max_length= 500)
    def list(self):
        self.name = list(name)

