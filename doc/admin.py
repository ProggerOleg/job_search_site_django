# Register your models here.
from django.contrib import admin
from .models import *


class JobListAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'time_create', 'salary', 'available')
    list_display_links = ('id', 'job_title')
    search_fields = ('job_title', 'content')
    list_editable = ('available',)
    list_filter = ('available', 'time_create')
    prepopulated_fields = {'slug': ('job_title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(JobList, JobListAdmin)
admin.site.register(Category, CategoryAdmin)