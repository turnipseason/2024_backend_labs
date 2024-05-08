from django.contrib import admin
from .models import Scientist, Book, Mineral
# Register your models here.

admin.site.register(Scientist)
admin.site.register(Book)
admin.site.register(Mineral)