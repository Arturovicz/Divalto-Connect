from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('plots/', views.view_plots, name='plots'),
    path('abouts/', views.view_abouts, name='abouts'),
    path('articles/', views.view_articles, name='articles'),
    path('articles/<int:page>/', views.view_articles, name='articles')
]


