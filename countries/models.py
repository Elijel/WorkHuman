import uuid
from django.db import models
from django.urls import reverse

class Continent(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'continent'
        verbose_name_plural = 'continents'

    def get_absolute_url(self):
        return reverse('countries:countries_by_continent', args=[self.id])

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='country', blank=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name