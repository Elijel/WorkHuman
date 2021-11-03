from django.urls import path
from . import views

app_name='countries'

urlpatterns = [
    path('', views.allContinents, name='allContinents'),
    path('<uuid:continent_id>/', views.allContinents, name='countries_by_continent'),
]