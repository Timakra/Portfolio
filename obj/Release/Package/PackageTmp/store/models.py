from django.db import models
from MySite.settings import BASE_DIR
from django_resized import ResizedImageField
from django.contrib.auth.models import User

# Create your models here.


class storeItems(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    sku = models.CharField(max_length=20,unique=True)
    image = ResizedImageField([500,300],crop=["middle","center"],upload_to='items/')
    shortdesc = models.CharField(max_length=30)
    longdesc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    dateAdded = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}  -  {}".format(self.name,self.sku)

    class Meta:
        ordering = ('dateAdded',)


class Specs(models.Model):
    item = models.ForeignKey(storeItems, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return  "{} {}  -  {}".format(self.title,self.item.name,self.item.sku)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(storeItems,  on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalprice = models.DecimalField(decimal_places=2,max_digits=20)

    def getprice():
        return self.quantity * self.item.price