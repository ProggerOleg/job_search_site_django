from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    companies = JobList.objects.all()
    return render(request, 'index.html', {'companies': companies} )

def cv_page(request):
    return render(request,'my_cv.html')