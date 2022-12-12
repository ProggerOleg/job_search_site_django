from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class JobList(models.Model):
    job_title = models.CharField(max_length=255, verbose_name='Назва')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Заробітня плата')
    job_description = models.TextField(verbose_name='Детальніше про вакансію')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації вакансії')
    available = models.BooleanField(default=True, verbose_name='Чи відкрита вакасія?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорія')
    company = models.ForeignKey('Company', on_delete=models.PROTECT, verbose_name="Назва компанії")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('vacancies', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'
        ordering = ['-time_create', 'job_title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=110, unique=True, db_index=True, verbose_name="Посилання")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id']


class Company(models.Model):
    company_name = models.CharField(max_length=100, db_index=True, verbose_name='Назва компанії')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_slug': self.slug})

    class Meta:
        verbose_name = 'Компанія'
        verbose_name_plural = 'Компанії'
        ordering = ['id']