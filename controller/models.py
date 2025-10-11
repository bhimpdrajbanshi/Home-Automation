from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)  # False = OFF, True = ON

    def __str__(self):
        return f"{self.name} - {'ON' if self.status else 'OFF'}"
