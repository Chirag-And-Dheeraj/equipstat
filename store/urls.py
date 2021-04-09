from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('instruments/', views.instruments, name="instruments"),
	path('calculators/', views.calculators, name="calculators"),
	path('refurbished-instruments/', views.refurbishedInstruments, name="refurbished-instruments"),
	path('refurbished-books/', views.refurbishedBooks, name="refurbished-books"),
	path('refurbished-labcoats/', views.refurbishedLabcoats, name="refurbished-labcoats"),
]

