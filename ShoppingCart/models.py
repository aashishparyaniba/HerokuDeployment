from django.db import models

from django.contrib.auth.models import User
from Products.models import ShowProducts
from Signupin.models import Customer
import datetime
# Create your models here.


class Order(models.Model):
    product = models.ForeignKey(ShowProducts, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=500, default="", blank=True)
    phone = models.CharField(max_length=101, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    paymentId = models.CharField(max_length=200, blank=True, null=True)


    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by("-date")