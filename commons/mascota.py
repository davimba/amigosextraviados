from django.db import models
from .publicacion import Publicacion

from third_party_apps.geoposition.fields import GeopositionField


class Mascota(Publicacion):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=400, verbose_name="Descripcion")
    position = GeopositionField(blank=True)

    def __str__(self):
        return u'%s %s' % (self.id, self.nombre)

    class Meta:
        abstract = True
