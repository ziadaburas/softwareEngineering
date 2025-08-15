from django.db import models


# Create your models here.
class Teacher(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=9)
    salary = models.DecimalField(max_digits=6, decimal_places=3)
    def __str__(self):
        return f"{self.firstName}_{self.lastName}"