from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)
    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"


class Registration(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices =(("M","Male") , ("F","Female") , ("Others","Prefer not to say"))
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dateofbirth=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table = "registration_table"


class Product(models.Model):
    id=models.AutoField(primary_key=True)
    category_choices = (("Bike-Spareparts", "Bike-Spareparts"), ("car-Spareparts","car-Spareparts"),("Others","Others"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product_table"

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50,blank=False,unique=True)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "feedback_table"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,blank=False,unique=True)
    phone = models.CharField(max_length=20)
    car_make_choice =(("W","WATER WASH" ),("S","CAR SERVICE"))
    car_make = models.CharField(blank=False, choices=car_make_choice, max_length=10)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField(null=True, blank=True, default=None)

    class Meta:
        db_table = "customers_table"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


