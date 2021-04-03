from django.shortcuts import render

from django.views import View
from Products.models import ShowProducts

# Create your views here.
class Products(View):

    def get(self, request):
        womenClothing = list(ShowProducts.objects.filter(Gender="2"))
        menClothing = list(ShowProducts.objects.filter(Gender="1"))
        return render(request, "productsHomepage.html", {"WomenImage0": womenClothing[0],
        "WomenImage1": womenClothing[1], "WomenImage2": womenClothing[2],
        "MenImage0": menClothing[0], "MenImage1": menClothing[1], "MenImage2": menClothing[2]})

