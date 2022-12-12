# Generated by Django 4.1.2 on 2022-12-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_alter_company_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='job_description',
            field=models.TextField(verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації вакансії'),
        ),
    ]
