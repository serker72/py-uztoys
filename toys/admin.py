from django.contrib import admin
from .models import Category, Product, ProductProperty, ProductPropertyValue, ProductImage, ProductReview, Contest, ContestImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductPropertyValueInline(admin.TabularInline):
    model = ProductPropertyValue
    
class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'enabled')
    
class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    
class ContestImageInline(admin.TabularInline):
    model = ContestImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'name', 'enabled')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'description', 'price', 'enabled')
    inlines = [
        ProductImageInline,
        ProductPropertyValueInline,
        ProductReviewInline,
    ]
    
class ContestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dt_start', 'dt_end', 'category', 'product')
    inlines = [
        ContestImageInline,
    ]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductProperty, ProductPropertyAdmin)
admin.site.register(Contest, ContestAdmin)
