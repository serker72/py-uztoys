from django.db import models
#from django.urls.base import reverse

class Category(models.Model):
    """
    Модель 'Категории'
    """

    # Fields
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, help_text="Выберите категорию верхнего уровня")
    name = models.CharField(max_length=255, help_text="Укажите наименование категории")
    enabled = models.BooleanField(help_text="Активность")
    photo = models.ImageField(null=True, upload_to='category', help_text="Выберите файл с изображением")

    # Metadata
    class Meta: 
        ordering = ["name"]

    # Methods
#    def get_absolute_url(self):
#         """
#         Returns the url to access a particular instance of Category.
#         """
#         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Category object (in Admin site etc.)
        """
        return self.name


class Product(models.Model):
    """
    Модель 'Изделия'
    """

    # Fields
    category = models.ForeignKey('Category', models.SET_NULL, blank=False, null=True, help_text="Выберите категорию")
    name = models.CharField(max_length=255, help_text="Укажите наименование изделия")
    description = models.TextField(help_text="Укажите описание изделия")
    price = models.DecimalField(decimal_places=2, max_digits=15, default=0.00, help_text="Укажите стоимость изделия")
    enabled = models.BooleanField(help_text="Активность")
    date_modified = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta: 
        ordering = ["name"]

    # Methods
#    def get_absolute_url(self):
#         """
#         Returns the url to access a particular instance of Category.
#         """
#         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Category object (in Admin site etc.)
        """
        return self.name


class ProductProperty(models.Model):
    """
    Модель 'Свойства изделий'
    """

    # Fields
    name = models.CharField(max_length=255, help_text="Укажите наименование свойства")
    description = models.TextField(blank=True, help_text="Укажите описание свойства")
    enabled = models.BooleanField(help_text="Активность")

    # Metadata
    class Meta: 
        ordering = ["name"]

    # Methods
#    def get_absolute_url(self):
#         """
#         Returns the url to access a particular instance of Category.
#         """
#         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Category object (in Admin site etc.)
        """
        return self.name


class ProductPropertyValue(models.Model):
    """
    Модель 'Значения свойств изделий'
    """

    # Fields
    product = models.ForeignKey('Product', blank=False, null=False, on_delete=models.CASCADE, help_text="Выберите изделие")
    property = models.ForeignKey('ProductProperty', blank=False, null=False, on_delete=models.CASCADE, help_text="Выберите свойство")
    val = models.CharField(max_length=255, help_text="Укажите значение свойства")

    # Metadata
#    class Meta: 
#        ordering = ["name"]

    # Methods
#    def get_absolute_url(self):
#         """
#         Returns the url to access a particular instance of Category.
#         """
#         return reverse('model-detail-view', args=[str(self.id)])
    
#    def __str__(self):
#        """
#        String for representing the Category object (in Admin site etc.)
#        """
#        return self.field_name


class ProductImage(models.Model):
    """
    Модель 'Изображения для изделий'
    """

    # Fields
    product = models.ForeignKey('Product', blank=False, null=False, on_delete=models.CASCADE, help_text="Выберите изделие")
    sort = models.PositiveSmallIntegerField(default=0, help_text="Укажите порядок следования изображения")
    description = models.CharField(blank=True, null=True, max_length=255, help_text="Укажите описание изображения")
    photo = models.ImageField(null=False, upload_to='product', help_text="Выберите файл с изображением")

    # Metadata
    class Meta: 
        ordering = ["sort"]


class Contest(models.Model):
    """
    Модель 'Конкурсы'
    """

    # Fields
    name = models.CharField(max_length=255, help_text="Укажите наименование конкурса")
    dt_start = models.DateField(help_text="Укажите дату начала конкурса")
    dt_end = models.DateField(null=True, help_text="Укажите дату окончания конкурса")
    description = models.TextField(blank=True, null=True, help_text="Укажите описание конкурса")
    product = models.ForeignKey('Product', blank=False, null=False, on_delete=models.CASCADE, help_text="Выберите изделие")
    category = models.CharField(blank=True, null=True, max_length=255, help_text="Укажите категорию конкурса для изделия")

    # Metadata
    class Meta: 
        ordering = ["dt_start"]


class ContestImage(models.Model):
    """
    Модель 'Изображения для конкурсов'
    """

    # Fields
    contest = models.ForeignKey('Contest', blank=False, null=False, on_delete=models.CASCADE, help_text="Выберите изделие")
    sort = models.PositiveSmallIntegerField(default=0, help_text="Укажите порядок следования изображения")
    description = models.CharField(blank=True, null=True, max_length=255, help_text="Укажите описание изображения")
    photo = models.ImageField(null=False, upload_to='contest', help_text="Выберите файл с изображением")

    # Metadata
    class Meta: 
        ordering = ["sort"]


class ProductReview(models.Model):
    """
    Модель 'Отзывы о изделии'
    """

    # Fields
    product = models.ForeignKey('Product', blank=False, null=False, on_delete=models.CASCADE, help_text="Выберите изделие")
    dt_create = models.DateTimeField(help_text="Укажите дату добавления отзыва")
    score = models.PositiveSmallIntegerField(default=0, help_text="Укажите оценку")
    user_name = models.CharField(max_length=255, help_text="Укажите имя пользователя")
    user_email = models.EmailField(blank=True, null=True, help_text="Укажите e-mail пользователя")
    description = models.TextField(help_text="Укажите текст отзыва")
    dt_moderation = models.DateTimeField(blank=True, null=True, help_text="Укажите дату модерации отзыва")
    enabled = models.BooleanField(help_text="Публиковать")

    # Metadata
    class Meta: 
        ordering = ["dt_create"]
