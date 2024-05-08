
from django.contrib import admin
from django.urls import path
from mainapp import views
from mainapp import drf_views

urlpatterns = [
    # legacy
    path('admin/', admin.site.urls),
    path('', views.index),
    path('people/', views.people),
    path('minerals/', views.minerals),
    path('index/', views.index),

    # 3-5
    path('add_book/', views.add_book),
    path('add_mineral/', views.add_mineral),
    path('add_scientist/', views.add_scientist),
    path('book/', views.book_search),
    path('mineral/', views.mineral_search),
    path('scientist/', views.scientist_search),


    # specifically for drf
    # if we don't write <pk> as <pk> --> 'Expected view to be called with a URL keyword argument named "pk"'
    path('drf_scientists/', drf_views.ScientistListCreateAPIView.as_view()),
    path('drf_scientists/<pk>/', drf_views.ScientistRetrieveUpdateDestroyAPIView.as_view()),
    path('drf_minerals/', drf_views.MineralListCreateAPIView.as_view()),
    path('drf_minerals/<pk>/', drf_views.MineralRetrieveUpdateDestroyAPIView.as_view()),
    path('drf_books/', drf_views.BookListCreateAPIView.as_view()),
    path('drf_books/<pk>/', drf_views.BookRetrieveUpdateDestroyAPIView.as_view()),

]
