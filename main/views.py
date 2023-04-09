from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Articles


@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def view_abouts(request):
    return render(request, 'main/abouts.html')

"""
@login_required(login_url="/login")
def view_articles(request):
    query = request.GET.get('q')
    if query:
        article_list = Articles.objects.filter(prod_label__icontains=query)
    else:
        article_list = Articles.objects.all()

    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'to_show/articles.html', {'articles': articles})

"""


@login_required(login_url="/login")
def view_articles(request):
    search_option = request.GET.get('search_option')
    query = request.GET.get('q')
    if query:
        if search_option == 'ref':
            articles = Articles.objects.filter(prod_ref__icontains=query)
        elif search_option == 'article_name':
            articles = Articles.objects.filter(prod_label__icontains=query)
        elif search_option == 'order_id':
            articles = Articles.objects.filter(order_id__icontains=query)
    else:
        articles = Articles.objects.all()

    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'articles': articles,
        'search_option': search_option,
        'query': query
    }

    return render(request, 'to_show/articles.html', context)


@login_required(login_url="/login")
def view_plots(request):
    return redirect("http://localhost:8501/")

