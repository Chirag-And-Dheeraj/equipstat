from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    academicDetails = models.TextField()
    contact = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.first_name


TYPES = ( ('1', 'Books'), ('2', 'Lab Coats'), ('3', 'Instruments') )


class ProductRefurbished(models.Model):
    name = models.CharField(max_length=50)
    seller = models.OneToOneField(UserDetail, on_delete=models.CASCADE)
    typeOfProduct = models.CharField(max_length=20, choices=TYPES)
    expectedReturn = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    details = models.TextField()

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

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name