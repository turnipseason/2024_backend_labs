from django.db import models
import datetime

# Create your models here.
class Scientist(models.Model):
    name = models.CharField(max_length=200, blank=False, help_text='ФИО')
    birth_year = models.DateField(default=datetime.date(1990,1,1), help_text='Дата рождения',
                                  blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, help_text='Страна', null=True)
    university = models.CharField(max_length=160, blank=True, help_text='Alma-mater', null=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Mineral(models.Model):
    name = models.CharField(max_length=60, blank=False)
    discovery_year = models.DateField(default=datetime.date(1990,1,1), help_text='Год открытия',
                                      null=True, blank=True)
    # null=True --> can be null in the DB; blank=True --> can be null in form
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE, related_name='minerals', null=True, blank=True)
    description = models.TextField(help_text='Описание', default='A precious stone', null=True, blank=True)
    def __str__(self) -> str:
        if self.scientist:
            return f'Название минерала: {self.name}\nГод открытия: {self.discovery_year}\nПервооткрыватель: {self.scientist}'
        return f'Название минерала: {self.name}\nГод открытия: {self.discovery_year}\nПервооткрыватель: Неизвестен'


class Book(models.Model):
    name = models.CharField(max_length=60, blank=False, help_text='Название монографии')
    publishing_year = models.DateField(default=datetime.date(1990,1,1), help_text='Год выпуска',
                                       null=True, blank=True)
    authors = models.ManyToManyField(Scientist, related_name='books', blank=True)
    description = models.TextField(help_text='Описание', default='Описание книги',null=True, blank=True)

    def __str__(self) -> str:
        authors_str = ', '.join([author.name for author in self.authors.all()])
        return f'Название книги: {self.name}\nГод выпуска: {self.publishing_year}\nАвторы: {authors_str}'
