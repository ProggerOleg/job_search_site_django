# Generated by Django 4.1.2 on 2022-12-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0006_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=110, unique=True, verbose_name='Посилання'),
        ),
    ]
