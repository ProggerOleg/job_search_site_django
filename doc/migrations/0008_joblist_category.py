# Generated by Django 4.1.2 on 2022-12-10 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='doc.category', verbose_name='Категорія'),
            preserve_default=False,
        ),
    ]
