from datetime import datetime

from django.db import models

from commande.models import Commande

"""Il s'agit ici de toutes les classes ayant un lien avec le module "Paiement" """

class TransactionPaypal(models.Model):
    paypal_order_id = models.CharField(max_length=100, unique=True, editable=False)
    paypal_capture_id = models.CharField(max_length=100, unique=True, editable=False)
    paypal_webhook_event_id = models.CharField(max_length=100, blank=True, editable=False)

    class Statut(models.TextChoices):
        CREATED = 'created', 'Créée'
        APPROVED = 'approved', 'Approuvée'
        CAPTURED = 'captured', 'Payée'
        FAILED = 'failed', 'Échouée'
        REFUNDED = 'refunded', 'Remboursée'

    status = models.CharField(max_length=10, choices=Statut.choices, editable=False)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    class Devise(models.TextChoices):
        FRANCS = 'francs', 'Francs CFA'
        EUROS = 'euros', 'EUROS'
        DOLLARS = 'dollars', 'DOLLARS AMERiCAINS'

    devise = models.CharField(max_length=10, choices = Devise.choices, editable=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_capture = models.DateTimeField(default=datetime.now)
    reponse_complete = models.JSONField()
    commande = models.OneToOneField(Commande, on_delete=models.PROTECT)
