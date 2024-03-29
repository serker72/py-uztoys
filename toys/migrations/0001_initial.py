# Generated by Django 2.1.2 on 2018-10-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.IntegerField(help_text='Выберите категорию верхнего уровня')),
                ('name', models.CharField(help_text='Укажите наименование категории', max_length=255)),
                ('enabled', models.BooleanField(help_text='Активность')),
            ],
            options={
                'ordering': ['parent', 'name'],
            },
        ),
    ]
