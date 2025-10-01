from django.db import models

# Create your models here.
class Laptop(models.Model):
    brand = models.CharField(max_length=100, default='ASUS')
    model_name = models.CharField(max_length=100, default='ROG Strix SCAR 18 G835LX-SA047W')
    processor = models.CharField(max_length=255, default='Intel Core Ultra 9 275HX')
    gpu = models.CharField(max_length=255, default='NVIDIA GeForce RTX 5090 Laptop GPU')
    ram = models.PositiveIntegerField(default=64)  # in GB
    storage = models.PositiveIntegerField(default=4)  # in TB
    display_size = models.PositiveIntegerField(default=18)  # in inches
    display_resolution = models.CharField(max_length=50, default='2560 x 1600')
    refresh_rate = models.PositiveIntegerField(default=240)  # in Hz
    operating_system = models.CharField(max_length=50, default='Windows 11 Home')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # in local currency

    def __str__(self):
        return f"{self.brand} {self.model_name} - {self.processor} / {self.gpu}"