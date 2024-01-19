from django.db import models

# Create your models here.
class Product(models.Model):
    urls = models.TextField(null=True)
    product_description = models.TextField(max_length=5000)
    image = models.URLField(null=True, blank=True)
    price = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.product_description
