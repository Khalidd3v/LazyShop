from django.shortcuts import render

def home(request):
 return render(request, 'mainapp/home.html')

def product_detail(request):
 return render(request, 'mainapp/productdetail.html')

def add_to_cart(request):
 return render(request, 'mainapp/addtocart.html')

def buy_now(request):
 return render(request, 'mainapp/buynow.html')

def profile(request):
 return render(request, 'mainapp/profile.html')

def address(request):
 return render(request, 'mainapp/address.html')

def orders(request):
 return render(request, 'mainapp/orders.html')

def change_password(request):
 return render(request, 'mainapp/changepassword.html')

def mobile(request):
 return render(request, 'mainapp/mobile.html')

def login(request):
 return render(request, 'mainapp/login.html')

def customerregistration(request):
 return render(request, 'mainapp/customerregistration.html')

def checkout(request):
 return render(request, 'mainapp/checkout.html')
