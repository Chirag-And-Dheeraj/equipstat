from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.first_name


class Book(models.Model):
    seller = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_of_publishing = models.IntegerField()
    price = models.FloatField()
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Book.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " | " + str(self.year_of_publishing)


class Instrument(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Instrument.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Instruments"


class Labcoat(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return str(self.size)

    class Meta:
        verbose_name_plural = "Labcoats"


class Product(models.Model):
    name = models.CharField(max_length=200)
    mrp = models.FloatField()
    seller_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    ourPrice = models.FloatField()
    inventory = models.IntegerField()
    slug = models.SlugField(max_length=250, null=True, blank=True)
    details = models.TextField()

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    @property
    def saving(self):
        return self.mrp - self.ourPrice

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"


class Order(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True)
    orderTotal = models.FloatField(null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    placed = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitemslist = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitemslist])
        return total

    @property
    def get_cart_items(self):
        orderitemlist = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitemslist])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    dateAdded = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def get_total(self):
        total = self.product.ourPrice * self.quantity
        return total


MESSAGE_TYPES = (('Grievance', 'Grievance'), ('Feedback', 'Feedback'))
STATUS_TYPES = (('Replied', 'Replied'), ('Resolved','Resolved'), ('Pending','Pending'), ('Spam','Spam'))

class ContactUsDetail(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=10, null=True)
    typeOfMessage = models.CharField(max_length=10, choices=MESSAGE_TYPES)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_TYPES, default='Pending')
    
    def __str__(self):
        return self.typeOfMessage + " | " + self.status