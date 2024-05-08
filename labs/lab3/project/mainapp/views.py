from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Scientist, Mineral

# Create your views here.

def index(request):
    return(render(request, 'mainapp/index.html'))

def people(request):
    people = Scientist.objects.all()
    return(render(request, 'mainapp/people.html', ))

def minerals(request):
    minerals = Mineral.objects.all()
    return(render(request, 'mainapp/minerals.html', ))

@require_GET
def book_search(request):
    name = request.GET.get('name')
    description = request.GET.get('description')
    param_filter = Q()

    if name:
        param_filter &= Q(name__icontains=name)
    if description:
        param_filter &= Q(name__icontains=description)

    books = Book.objects.filter(param_filter)

    found_books = []

    for book in books:
        authors_info = [{'name': author.name, 'university': author.university} for author in book.authors.all()]
        book_info = {
            'name': book.name,
            'publishing_year': book.publishing_year,
            'description': book.description,
            'authors': authors_info
        }
        found_books.append(book_info)

    return JsonResponse({'books': found_books})

@require_GET
def mineral_search(request):
    name = request.GET.get('name')
    param_filter = Q()
    if name:
        param_filter &= Q(name__icontains=name)

    minerals = Mineral.objects.filter(param_filter)

    filtered_minerals = [{'name': mineral.name, 'discovery_year': mineral.discovery_year} for mineral in minerals]
    return JsonResponse({'minerals': filtered_minerals})

@require_GET
def scientist_search(request):
    name = request.GET.get('name')
    uni = request.GET.get('uni')
    country = request.GET.get('country')

    param_filter = Q()

    if name:
        param_filter &= Q(name__icontains=name)
    if uni:
        param_filter &= Q(university__icontains=uni)
    if country:
        param_filter &= Q(country__icontains=country)

    scientists = Scientist.objects.filter(param_filter)
    filtered_people = [{'name': scientist.name, 'university': scientist.university,
                        'country' : scientist.country} for scientist in scientists]
    return JsonResponse({'scientists': filtered_people})


# so that curl (posting) doesn't fail with a 403 error
@csrf_exempt
@require_POST
def add_book(request):
    name = request.POST.get('name')
    publishing_year = request.POST.get('publishing_year')
    authors_names = request.POST.getlist('author')
    description = request.POST.get('description')

    authors = []
    for author_name in authors_names:
        scientist = Scientist.objects.filter(name=author_name).first()
        if scientist:
            authors.append(scientist)
        else:
            new_author = Scientist.objects.create(name=author_name)
            authors.append(new_author)

    new_book = Book.objects.create(name=name, publishing_year=publishing_year, description=description)

    new_book.authors.add(*authors)
    return JsonResponse({'message': '\nBook added successfully'})

@csrf_exempt
@require_POST
def add_scientist(request):
    name = request.POST.get('name')
    birth_year = request.POST.get('birth_year')
    country = request.POST.get('country')
    university = request.POST.get('university')

    new_scientist = Scientist.objects.create(name=name, birth_year=birth_year, country=country, university=university)
    return JsonResponse({'message': '\nWelcoming a new scientist!'})

@csrf_exempt
@require_POST
def add_mineral(request):
    name = request.POST.get('name')
    discovery_year = request.POST.get('discovery_year')
    scientist_name = request.POST.get('scientist')
    description = request.POST.get('description')

    scientist = Scientist.objects.filter(name=scientist_name).first()

    if scientist:
        new_mineral = Mineral.objects.create(name=name, discovery_year=discovery_year,
                                         scientist_id=scientist.id, description=description)
    else:
        new_mineral = Mineral.objects.create(name=name, discovery_year=discovery_year,description=description)

    return JsonResponse({'message': '\nMineral added successfully'})
