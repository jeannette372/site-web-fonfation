from django.contrib import admin

from catalogue.models import Livre, Categorie, Auteur

admin.site.register(Livre)
admin.site.register(Categorie)
admin.site.register(Auteur)
