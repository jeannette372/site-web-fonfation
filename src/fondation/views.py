from django.shortcuts import render

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