from django.shortcuts import render, get_object_or_404
from .models import Continent, Country
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def allContinents(request, continent_id=None):
    c_page = None
    countries_list = None
    if continent_id != None:
        c_page = get_object_or_404(Continent, id=continent_id)
        countries_list = Country.objects.filter(continent=c_page)
    else:
        countries_list = Country.objects.all().filter()

    '''Pagination Code'''
    paginator = Paginator(countries_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        countries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        countries = paginator.page(paginator.num_pages)
    return render(request,'continents/continent.html',{'continent':c_page,'countries':countries})
