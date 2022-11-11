from django.db import models

# Create your models here.

class todo(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    Date = models.DateField()

    def __str__(self):
        return self.name