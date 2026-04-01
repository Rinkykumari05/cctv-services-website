from django.contrib import admin
from .models import Inquiry, Product, Package, Testimonial, Gallery

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'property_type', 'created_at']
    search_fields = ['name', 'phone', 'property_type']
    list_filter = ['property_type', 'created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'created_at']
    search_fields = ['name']

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'is_featured']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'created_at']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']