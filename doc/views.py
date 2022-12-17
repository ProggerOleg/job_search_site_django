from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import RegisterUserForm
from .models import *

def index(request):
    vacancies = JobList.objects.all()
    return render(request, 'index.html', {'vacancies': vacancies, 'title': 'Jobfinder.ua'})

def cv_page(request):
    return render(request,'my_cv.html', {'title': 'Моє резюме'})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        return {'title': 'Авторизація', 'form': self.form_class}

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        return {'title': 'Регистрація', 'form': self.form_class}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('login')

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

class UserProfile(DetailView):
    model = 4 #Не забыть подсоеденить моделю юзера

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
