from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    rating = models.IntegerField(default=2, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.title
