from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class_name = models.ManyToManyField(Class)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name