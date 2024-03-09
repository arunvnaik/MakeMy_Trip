from django.db import models
from django.core.validators import MinValueValidator


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    email = models.EmailField(unique=True)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.location_name

class Cost(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE, primary_key=True, related_name='cost')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.location} - {self.price}"
    

