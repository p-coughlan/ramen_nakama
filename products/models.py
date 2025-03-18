from django.db import models

class Category(models.Model):
    """
    A model for the product categories
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Returns the name of the category """
        return self.name
    
    def get_friendly_name(self):
        """ Returns the friendly name of the category """
        return self.friendly_name
    
class Product(models.Model):
    """
    A model for the products
    null = True allows the field to be optional
    blank = True allows the field to be optional in forms
    on_delete=models.SET_NULL sets the value of the foreign key to NULL if the associated record in the referenced table is deleted
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ Returns the name of the product """
        return self.name