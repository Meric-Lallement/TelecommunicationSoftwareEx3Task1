from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def Hello(request):
    return HttpResponse("Hello World ! I am coming")

def file(request):
    return FileResponse(open(os.path.join(BASE_DIR,"helloapp/templates/CalendrierRTU.pdf"), 'rb'), as_attachment=True)

def redirectHTTP(request):
    return HttpResponseRedirect("https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal")