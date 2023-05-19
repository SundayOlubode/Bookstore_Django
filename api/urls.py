from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('books/', views.getBooks),
    path('add_book/', views.postBook),
    path('authors/', views.getAuthors)
]