# Generated by Django 2.1.2 on 2018-10-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0008_productpropertyvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(help_text='Изображение', null=True, upload_to='category'),
        ),
    ]