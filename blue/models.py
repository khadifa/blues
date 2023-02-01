from django.db import models

# Create your models here.

class Products(models.Model):
    PortName = models.CharField(max_length = 30)
    Contact = models.CharField(max_length = 30)
    Location = models.CharField(max_length = 30)
    Status = models.CharField(max_length = 30)

    def __str__(self):
        return self.PortName
