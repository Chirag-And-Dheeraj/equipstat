from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('product/', views.product, name="product"),
]

