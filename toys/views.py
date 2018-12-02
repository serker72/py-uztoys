#from django.db.models import Prefetch
from django.shortcuts import render
from django.views import generic
from django.conf import settings
from .models import Category, Product, Contest
#ProductImage, 

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Получение списка активных категорий верхнего уровня
    categories=Category.objects.all().filter(enabled=1, parent__isnull=True)
    
    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
    return render(
        request,
        'index.html',
        context={'categories':categories, 'mediaPath':settings.MEDIA_URL},
    )

def category(request, categoryid):
    """
    Функция отображения страницы категории
    """
    # Получение объекта категории
    currentCategory = Category.objects.get(id=categoryid)
    # Получение списка активных подкатегорий категорий
#    categories=Category.objects.all().filter(enabled=1, parent=categoryid)
    categories=Category.objects.all().filter(enabled=1)
    # Получение списка активных изделий
    products=Product.objects.all().filter(enabled=1, category=categoryid)
#    .prefetch_related(Prefetch('productimage', queryset=ProductImage.objects.all()))
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'category.html',
        context={'currentCategory':currentCategory, 'categories':categories, 'products':products, 'mediaPath':settings.MEDIA_URL},
    )

class ProductDetailView(generic.DetailView):
    model = Product
 
#    def get_queryset(self):
#        category_id = self.kwargs['category']
#        return Product.objects.filter(category=category_id)
    
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['mediaPath'] = settings.MEDIA_URL
        return context

class ContestListView(generic.ListView):
    model = Contest
    