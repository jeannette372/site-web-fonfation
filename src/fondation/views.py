from django.shortcuts import render, redirect

from catalogue.models import Livre

def index(request):
    return render(request, "index.html")

def apropos(request):
    return render(request, "apropos.html")

def livres(request):
    return render(request, "Livres.html")

def bracelets(request):
    return render(request, "Bracelets.html")

def studio(request):
    return render(request, "Studio.html")

def contact(request):
    return render(request, "Contact.html")

# def ajouter_livre(request):
#     if request.method == "POST":
#         titre = request.POST.get("titre")
#         # auteur = request.POST.get("auteur")
#         livre, created = Livre.objects.get_or_create(titre=titre, slug=titre.lower())
#
#         print("Ajout réussi")
