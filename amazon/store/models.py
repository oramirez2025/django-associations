from django.db import models





class User(models.Model):
    # shop = models.ManyToManyField('Shop', through='Review')
    pass
class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ManyToManyField(User, related_name='reviewed_products')

