from django.urls import path
     from . import views
     urlpatterns = [
         path('', views.product_list, name='product_list'),
         path('cart/', views.cart, name='cart'),
         path('order_history/', views.order_history, name='order_history'),
     ]