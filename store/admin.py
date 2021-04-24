from django.contrib import admin
from .models import *



# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Instrument)
admin.site.register(Labcoat)
admin.site.register(BookImage)
admin.site.register(LabcoatImage)
admin.site.register(InstrumentImage)
admin.site.register(ContactUsDetail)
admin.site.register(Order)
admin.site.register(OrderItem)