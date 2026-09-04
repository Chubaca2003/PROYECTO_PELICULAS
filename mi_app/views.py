from django.conf import settings
from django.shortcuts import render


def inicio(request):
    if not settings.SISTEMA_ABIERTO:
        return render(request, 'no_dispo.html', status=503)
    return render(request, 'index.html')
