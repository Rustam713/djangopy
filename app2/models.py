from django.db import models

# Create your models here.
class Simple(models.Model):
    name = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.name)