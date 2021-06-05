from django.db import models

# Create your models here.
class Customer(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Phone = models.CharField(max_length=11)
    Email = models.EmailField()
    Password = models.CharField(max_length=1000)

    def isExists(self):
        if Customer.objects.filter(Email = self.Email):
            return True
        
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(Email=email)
        except:
            return False