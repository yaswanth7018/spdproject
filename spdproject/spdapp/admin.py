from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Registration, Admin, Product, Feedback, Customer

admin.site.register(Admin)
admin.site.register(Registration)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(Customer)

