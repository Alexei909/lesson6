from django.shortcuts import render
from django.http import HttpResponse
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.all()
    context = {'title': 'Урок 6',
               'menu': menu,
               'posts': posts
}
    
    return render(request, 'core/index.html', context=context)

def about(request):
    return render(request, 'core/about.html', {'title': 'О сайте'})

def add_page(request):
    return HttpResponse("Добавление страницы")

def login(request):
    return HttpResponse("Войти")

def contact(request):
    return HttpResponse("Обратная связь")