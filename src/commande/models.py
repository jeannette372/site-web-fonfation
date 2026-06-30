from datetime import timedelta

from django.db import models

from catalogue.models import Livre
from fondation.settings import AUTH_USER_MODEL

import uuid

"""Il s'agit ici de tout ce qui a un lien avec le module "Commande" """

class Commande(models.Model):
    reference = models.CharField(max_length=20, unique=True)
    date_de_commande = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    class Devise(models.TextChoices):
        FRANCS = 'francs', 'Francs CFA'
        EUROS = 'euros', 'EUROS'
        DOLLARS = 'dollars', 'DOLLARS AMERiCAINS'

    devise = models.CharField(max_length=10, choices=Devise.choices, default=Devise.FRANCS)

    class Statut(models.TextChoices):
        EN_ATTENTE = 'en_attente', 'Paiement en attente'
        PAYE = 'paye', 'Paiement fait'
        ECHEC = 'echec', 'Ecehc de la commande'

    status = models.CharField(max_length=10, choices=Statut.choices, default=Statut.EN_ATTENTE)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    utilisateur =  models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)

class LigneDeCommande(models.Model):
    class Format(models.TextChoices):
        PDF = "pdf", "Format PDF"
        EPUB = "epub", "Format EPUB"

    format = models.CharField(max_length=5, choices=Format.choices)
    prix_actuel = models.DecimalField(max_digits=10, decimal_places=2)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.PROTECT)

class LienTelechargement(models.Model):
    token = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    class Format(models.TextChoices):
        PDF = "pdf", "Format PDF"
        EPUB = "epub", "Format EPUB"

    format = models.CharField(max_length=5, choices=Format.choices)
    nombre_telechargements = models.PositiveSmallIntegerField(default=0)
    max_telechargements = models.PositiveSmallIntegerField(default=3)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    # date_expiration = date_de_creation + timedelta(hours=1)
    adresse_ip =  models.GenericIPAddressField(blank=True, null=True)
    status = models.BooleanField(default=True)
    ligne = models.ForeignKey(LigneDeCommande, on_delete=models.CASCADE)

