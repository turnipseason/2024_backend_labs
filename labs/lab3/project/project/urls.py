
from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('people/', views.people),
    path('minerals/', views.minerals),
    path('index/', views.index),
    path('add_book/', views.add_book),
    path('add_mineral/', views.add_mineral),
    path('add_scientist/', views.add_scientist),
    path('get_book/', views.book_search),
    path('get_mineral/', views.mineral_search),
    path('get_scientist/', views.scientist_search),
]
