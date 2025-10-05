from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


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
        return f"{self.brand} {self.model_name}"



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.user} "
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    quntity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.laptop} X {self.quntity}"

    @property
    def total_price(self):
        return self.laptop.price * self.quntity


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="order")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="pending")
    invoice_number = models.CharField(max_length=50, blank=True, null=True)
    paygiri = models.CharField(max_length=50, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.cart.user} ({self.status})" 
    
    @property
    def total_price(self):
        return self.cart.total_price