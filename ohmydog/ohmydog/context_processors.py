from django.core.exceptions import ObjectDoesNotExist
from donaciones import models
import json


def objeto_context(request):
    try:
        ultima_campana = models.Campaña.objects.latest('id')
    except ObjectDoesNotExist:
        ultima_campana = None
    return {'campana': ultima_campana}

def redes(request):
    with open("ohmydogApp/redes.json") as redes:
        datos_redes = json.load(redes)
    redes_sociales = datos_redes['redes_sociales']
    formas_contacto = datos_redes['formas_contacto']
    
    facebook = redes_sociales[0]['enlace']
    twitter = redes_sociales[1]['enlace']
    instagram = redes_sociales[2]['enlace']
    mail = formas_contacto[0]['dato']
    telefono = formas_contacto[1]['dato']

    return {
        'facebook': facebook,
        'twitter': twitter,
        'instagram': instagram,
        'mail': mail,
        'telefono': telefono
    }