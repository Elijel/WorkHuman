from .models import Continent

def menu_links(request):
    links= Continent.objects.all()
    return dict(links=links)