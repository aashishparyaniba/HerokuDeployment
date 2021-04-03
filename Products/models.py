from django.db import models


GENDER_CHOICES = (
    ("1", "Men"),
    ("2", "Women")
)

# Create your models here.
class ShowProducts(models.Model):
    Image = models.ImageField()
    ProductName = models.CharField(max_length=1000)
    CurrentPrice = models.DecimalField(decimal_places=2, max_digits=5)
    PastPrice = models.DecimalField(decimal_places=2, max_digits=5)
    OFF = models.IntegerField()
    Gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="1")

    def __str__(self):
        return self.ProductName

    class Meta:
        verbose_name_plural = "All Products"

