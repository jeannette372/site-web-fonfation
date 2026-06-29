from django.db import models
from datetime import datetime

from catalogue.models import Livre
from fondation.settings import AUTH_USER_MODEL

# Il s'agit ici de toutes les classes portant sur le module "panier"
"""
Infos sur la classe Panier
- Date de creation 
- Date de mise a jour 
- ID du client

"""

class Panier(models.Model):
    date_de_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)


class Article(models.Model):
    class Format(models.TextChoices):
        PDF = "pdf", "Format PDF"
        EPUB = "epub", "Format EPUB"

    format = models.CharField(max_length=5, choices=Format.choices)
    prix_actuel = models.PositiveIntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.PROTECT)

