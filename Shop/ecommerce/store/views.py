from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem

     def product_list(request):
         products = Product.objects.all()
         return render(request, 'store/product_list.html', {'products': products})

     def cart(request):
         order, created = Order.objects.get_or_create(user=request.user)
         return render(request, 'store/cart.html', {'order': order})

     def order_history(request):
         orders = Order.objects.filter(user=request.user)
         return render(request, 'store/order_history.html', {'orders': orders})
