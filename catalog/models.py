from django.db import models


# Create your models here.


class Category(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a product category (e.g. Appliances, Computers & Accessories, Books etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
from django_countries.fields import CountryField

class Brand(models.Model):
    """
    Model representing a brand.
    """
    name = models.CharField(max_length=100)
    country = CountryField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular brand instance.
        """
        return reverse('brand-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
        
        
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Product(models.Model):
    """
    Model representing a product
    """
    title = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True )
    # Foreign Key used because item can only have one brand, but brands can have multiple items
    summary = models.TextField(max_length=1000, help_text="Enter a brief product description")
    price = models.DecimalField('Price (USD)', max_digits=6, decimal_places=2) 
    category = models.ManyToManyField(Category, help_text="Select a category for this product")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, db_index=True, default='')

    
    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular item instance.
        """
        return reverse('item-detail', args=[str(self.id)])
        

    def display_category(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ category.name for category in self.category.all()[:3] ])
    display_category.short_description = 'Category'

        
from djmoney.models.fields import MoneyField

class Price(models.Model):
    
    some_currency = MoneyField( decimal_places=2, default=0, default_currency='USD', max_digits=11)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.some_currency)
        



