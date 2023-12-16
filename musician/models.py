from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    firstName = models.CharField(max_length=56)
    lastName = models.CharField(max_length=56)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=18)
    instrumentType = models.CharField(max_length=56)

    def __str__(self) -> str:
        return f"Name: {self.firstName} {self.lastName}"