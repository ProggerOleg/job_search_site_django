from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login', LoginUser.as_view(), name='login'),
    path('vacancies', vacancies_page, name='vacancies'),
    ]