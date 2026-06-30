from django.contrib import admin

from commande.models import Commande, LigneDeCommande, LienTelechargement

admin.site.register(Commande)
admin.site.register(LigneDeCommande)
admin.site.register(LienTelechargement)
