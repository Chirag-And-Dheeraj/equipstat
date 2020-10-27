from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.first_name


TYPES = ( ('1', 'Books'), ('2', 'Lab Coats'), ('3', 'Instruments') )


class ProductRefurbished(models.Model):
    name = models.CharField(max_length=50)
    seller = models.CharField(max_length=50 ,null=True)
    typeOfProduct = models.CharField(max_length=20, choices=TYPES)
    expectedReturn = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images/',null=True, blank=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    details = models.TextField()

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while ProductNew.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
	    return self.name




class ProductNew(models.Model):
    name = models.CharField(max_length=100)
    mrp = models.FloatField()
    ourPrice = models.FloatField()
    inventory = models.IntegerField()
    image = models.ImageField()
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    details = models.TextField()

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while ProductNew.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name



class Order(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True)
    orderTotal = models.FloatField(null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
        
    @property
    def get_cart_total(self):
        orderitems = self.orderlineitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
        
    @property
    def get_cart_items(self):
        orderitems = self.orderlineitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductNew, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    dateAdded = models.DateTimeField(auto_now_add=True ,null=True)
    
    @property
    def get_total(self):
        total = self.product.ourPrice * self.quantity
        return total


MESSAGE_TYPES = ( ('1', 'Grievance'), ('2', 'Feedback') )

class ContactUsDetail(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=10, null=True)
    typeOfMessage = models.CharField(max_length=10, choices=MESSAGE_TYPES)
    message = models.TextField()