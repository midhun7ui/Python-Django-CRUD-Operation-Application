from django.db import models

# Create your models here.


class Cource(models.Model):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.name
