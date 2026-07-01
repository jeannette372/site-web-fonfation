from django.db import models

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
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="utilisateur")

    def __str__(self):
        return f"Panier de l'utilisateur {self.utilisateur.username} crée {self.date_de_creation}"

class Article(models.Model):
    class Format(models.TextChoices):
        PDF = "pdf", "Format PDF"
        EPUB = "epub", "Format EPUB"

    format = models.CharField(max_length=5, choices=Format.choices)
    prix_actuel = models.PositiveIntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, related_name="panier")
    livre = models.ForeignKey(Livre, on_delete=models.PROTECT, related_name="livre_article")

    def __str__(self):
        return f"{self.livre.titre} du panier de l'utilisateur {self.panier.utilisateur.username} au prix de {self.prix_actuel}"

