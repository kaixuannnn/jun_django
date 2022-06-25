from django.db import models
from pkg_resources import require

class Product(models.Model):
    title = models.CharFlied(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER =' S'
    MEMBERSHIP_GOLD ='G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'), 
        (MEMBERSHIP_SILVER, 'Silver'), 
        (MEMBERSHIP_GOLD, 'Gold')
        ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES, 
        default=MEMBERSHIP_BRONZE
     )

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE='C'
    PAYMENT_FAILED='F'
    PAYMENT_STATUS=[
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed')
    ]
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING
        )

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer= models.OneToOneField(Customer, on_delete=models.CASCADE, priamry_key=True)