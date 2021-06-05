from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from django.views import View
from Products.models import ShowProducts
import razorpay
from ShoppingCart.models import Order
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Products.middlewares.auth import auth_middleware

# Create your views here.

class Homepage(View):

    def get(self, request):
        laptops = ShowProducts.objects.all()
        context = {
            "laptops": laptops,
        }
        print(request.session.get("customer"))
        return render(request, "productsHomepage.html", context)
    
    
    def post(self, request):
        gettingProduct = request.POST.get("laptop")
        request.session["laptopProduct"] = gettingProduct
        print(request.session.get("laptopProduct"))
        return redirect("checkoutPage")


class WomenProductPage(View):

    def get(self, request):
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        productsInfo = list(ShowProducts.objects.all())
        context = {"womenproducts": productsInfo}
        return render(request, "womenProducts.html", context)

    def post(self, request):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart
        print(request.session["cart"])

        return redirect("womensProductPage")



class ProductsDetailPage(View):

    def get(self, request, id):
        obj = get_object_or_404(ShowProducts, pk=id)
        context = {"obj": obj}
        return render(request, "productDetailPage.html", context)
        
    def post(self, request, id):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart
        print(request.session["cart"])

        return redirect("/women/"+str(id))

class CheckoutPage(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        sessionGettingProduct = request.session.get("laptopProduct")
        productById = ShowProducts.get_products_by_id(sessionGettingProduct)
        context = {
            "productCheckout": productById,
        }
        return render(request, "checkout.html", context)
    
    def post(self, request):
        
        # Razorpay Implementation
        productAmt = request.POST.get("totalAmt")
        order_amount = productAmt
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        
        client = razorpay.Client(auth=("rzp_test_G1jXAHHxcitb1c", "OBWdRbrbITmt08F3aQQkF7L3"))
        payment = client.order.create({"amount":order_amount, "currency":order_currency, "receipt":order_receipt})
        print(payment)
    
        return HttpResponse("Thankyou")