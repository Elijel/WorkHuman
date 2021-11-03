from django.shortcuts import render
from countries.models import Country
from django.db.models import Q

def searchResult(request):
    countries = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        countries = Country.objects.all().filter(Q(name__contains=query))
    return render(request, 'search.html', {'query':query, 'countries':countries})