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
	path('accounts/data', views.collectUserData, name="collect-user-data"),
    path('enlist/', views.enlist, name="enlist"),
	path('enlist/book', views.enlistBooks, name="enlist-books"),
    path('enlist/instrument', views.enlistInstruments, name="enlist-instruments"),
    path('enlist/labcoat', views.enlistLabcoats, name="enlist-labcoats"),
]

