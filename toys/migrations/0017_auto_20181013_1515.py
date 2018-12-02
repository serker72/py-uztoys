# Generated by Django 2.1.2 on 2018-10-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0016_productreview_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='category',
            field=models.CharField(blank=True, help_text='Укажите категорию конкурса для изделия', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='description',
            field=models.TextField(help_text='Укажите текст отзыва'),
        ),
    ]