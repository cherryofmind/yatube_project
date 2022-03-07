from django.shortcuts import HttpResponse

# Create your views here.

def group_post(request, slug):
    return HttpResponse('страница с постами, отфильтрованными по группам')

def index(request):
    return HttpResponse('Главная страница')