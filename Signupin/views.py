from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Signupin.models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

class Signup(View):

    def get(self, request):
        form = CreateUserForm()
        context = {"form": form}
        
        return render(request, "signup.html", context)
 
    def post(self, request):
        postData = request.POST
        firstName = postData.get("firstname")
        lastName = postData.get("lastname")
        phone = postData.get("phone")
        email = postData.get("email")
        password = postData.get("password")

        
        value = {
            "firstName": firstName,
            "lastName": lastName,
            "phone": phone,
            "email": email,
        }

        error_message = None


        customer = Customer(Firstname=firstName, Lastname=lastName, Phone=phone, Email=email, Password=password)

        if (not firstName):
            error_message = "First Name is Required"
        elif len(firstName) < 4:
            error_message = "First Name must be 4 Char Long"
        elif not lastName:
            error_message = "Last Name Required"
        elif len(lastName) < 4:
            error_message = "Last Name must be 4 Char Long"
        elif not phone:
            error_message = "Phone Number is Required"
        elif len(phone) < 10:
            error_message = "Phone Number must be 10 Char Long"
        elif not email:
            error_message = "Email is Required"
        elif not "@gmail.com" in email:
            error_message = "Make sure to end your email with '@gmail.com"
        elif not password:
            error_message = "Password is Required"
        elif len(password) < 6:
            error_message = "Length of Password must be Atleast 6 Characters"
        elif customer.isExists():
            error_message = "Email Address Already Registered.."

        if not error_message:
            customer.Password = make_password(customer.Password)
            customer.save()

            return redirect("home")
        else:
            data = {
                "error": error_message,
                "values": value,
            }
            return render(request, "signup.html", data)

        return HttpResponse("SignUp Success")

class Signin(View):

    def get(self, request):
        context = {}
        return render(request, "signin.html", context)

    def post(self, request):
            email = request.POST.get("email")
            password = request.POST.get("password")
            customer = Customer.get_customer_by_email(email)
                        
            error_message = None

            if customer:
                flag = check_password(password, customer.Password)
                if flag:
                    request.session["customer"] = customer.id
                    request.session["email"] = customer.Email
                    request.session["fullname"] = customer.Firstname + customer.Lastname

                    return redirect("home")
                else:
                    error_message = "Email or Password is Incorrect"
            else:
                error_message = "Email or Password is Incorrect"
                
            return render(request, "signin.html", {"error": error_message})

           
class Logout(View):

    def get(self, request):
        logout(request)
        return redirect("home")






        