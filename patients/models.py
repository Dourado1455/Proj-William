from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
