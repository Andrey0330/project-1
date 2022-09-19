from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Women, Category

# menu = [
#     {'title': 'О сайте', 'url_name': 'about'},
#     {'title': 'Добавить статью', 'url_name': 'addpage'},
#     {'title': 'Обратная связь', 'url_name': 'contact'},
#     {'title': 'Войти', 'url_name': 'login'},
# ]


def index(request):
    posts = Women.objects.filter(is_published=True)
    context = {
        # 'menu': menu,
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'Страница о нас'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id, is_published=True)

    if len(posts) == 0:
        raise Http404()

    context = {
        # 'menu': menu,
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,

    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')