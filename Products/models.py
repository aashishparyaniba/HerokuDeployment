from django.db import models




CATEGORIES = (
    ("Laptop", "Laptop"),
)

STOCKDETAILS = (
    ("In Stock", "In Stock"), 
    ("Out of Stock", "Out of Stock"),
)


# Create your models here.
class ShowProducts(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    Category = models.CharField(max_length=356, choices=CATEGORIES)
    StockDetails = models.CharField(max_length=356, choices=STOCKDETAILS)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "All Products"

    def get_absolute_url(self):
        return f"women/{{self.id}}/"

    @staticmethod
    def get_products_by_id(id):
        return ShowProducts.objects.filter(id=id)




    