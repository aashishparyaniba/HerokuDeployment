from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.

from django.views import View
from django.shortcuts import render, redirect
from Products.models import ShowProducts
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cart.cart import Cart
from django.contrib.sessions.backends.db import SessionStore
from .models import Order
import razorpay
from Signupin.models import Customer



class Cart(View):
    login_required(login_url="signin")
    def get(self, request):
        products = ""
        try:
            ids = list(request.session.get("cart").keys())
            products = ShowProducts.get_products_by_id(ids)
            
        except:
            pass
        context = {"products": products}
        return render(request, "cart.html", context)

    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = ShowProducts.get_products_by_id(list(cart.keys()))
        totalAmt = request.POST.get("totalAmt")

        order_amount = totalAmt
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        
        client = razorpay.Client(auth=("rzp_test_G1jXAHHxcitb1c", "OBWdRbrbITmt08F3aQQkF7L3"))
        payment = client.order.create({"amount":order_amount, "currency":order_currency, "receipt":order_receipt})
        
        print(payment)
        request.session["cart"] = {}
        

        for product in products:
            order = Order(customer = Customer(id=customer),
                        product = product,
                        price = product.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)))

            order.save()
        return HttpResponse("paymentsuccess")



class OrderView(View):
    def get(self, request):
        
        customer = request.session.get("customer")
        orders = Order.get_orders_by_customer(customer)
        
        context = {"orders": orders}
        return render(request, "orders.html", context)


class paymentSuccess(View):
    def get(self, request):
        return render(request, "paymentSuccess.html")