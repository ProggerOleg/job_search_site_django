from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *

def index(request):
    vacancies = JobList.objects.all()
    return render(request, 'index.html', {'vacancies': vacancies})

def cv_page(request):
    return render(request,'my_cv.html')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        return {'title': 'Авторизация', 'form': self.form_class}


def vacancies_page(request):
    # Shows the shopping page
    vacancies = JobList.objects.all().order_by('-time_create')
    paginator = Paginator(vacancies, 8)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        page_obj = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц,
        # возвращаем последнюю.
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'vacancies.html',
                  {'page': page,
                   'title': 'Вакансії',
                   'vacancies': page_obj, 'page_obj': page_obj})
