from django.db import models

"""Il s'agit de toutes les classes portant sur le catalogue"""

class Categorie(models.Model):
    nom = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    #orde_affichage = models.PositiveInteger(default=0)

class Livre(models.Model):
    titre = models.CharField(max_length=300)
    sous_titre = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    titre = models.CharField(max_length=300)
    isbn_numerique = models.CharField(max_length=20, blank=True)
    prix = models.PositiveIntegerField()
    langue = models.CharField(max_length=20)
    date_publication = models.DateField(blank=True)
    note_moyenne = models.DecimalField(max_digits=3, decimal_places=2)
    nombre_ventes = models.PositiveIntegerField(default=0)

    class Statut(models.TextChoices):
        PUBLIE = 'publie', 'Livre Publié'
        BROUILLON = 'brouillon', 'Brouillon'
        ARCHIVE = 'archive', 'Une archive'
    status = models.CharField(max_length=10, choices=Statut.choices)
    date_ajout = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)


class Auteur(models.Model):
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    biographie = models.TextField(blank=True)
    pays = models.CharField(blank=True)
