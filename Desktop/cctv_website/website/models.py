from django.db import models

class Inquiry(models.Model):
    PROPERTY_CHOICES = [
        ('Home', 'Home'),
        ('Shop', 'Shop'),
        ('Office', 'Office'),
        ('Warehouse', 'Warehouse'),
        ('School', 'School'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    property_type = models.CharField(max_length=20, choices=PROPERTY_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    features = models.TextField(help_text="Enter features separated by commas")
    is_featured = models.BooleanField(default=False)

    def get_features_list(self):
        return [feature.strip() for feature in self.features.split(',')]

    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title