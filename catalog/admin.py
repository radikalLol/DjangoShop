from django.contrib import admin

# Register your models here.

from .models import Brand, Category, Product, Price

#admin.site.register(Product)
#admin.site.register(Brand)

admin.site.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('name', 'country')

#admin.site.register(Brand, BrandAdmin)

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display_brand', 'price', 'display_category', 'stock', 'available')
    list_filter = ('brand', 'category','available')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    
#admin.site.register(Category)
#admin.site.register(Price)
