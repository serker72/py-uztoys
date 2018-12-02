from django import template

register = template.Library()

from ..models import Category, Product

@register.simple_tag
def get_main_categories():
    return Category.objects.all().filter(enabled=1, parent__isnull=True)

@register.simple_tag
def get_last_products():
    return Product.objects.all().filter(enabled=1).order_by('-date_modified')[:12]
