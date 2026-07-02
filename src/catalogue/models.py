from django.db import models

"""Il s'agit de toutes les classes portant sur le catalogue"""

class Categorie(models.Model):
    nom = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    #orde_affichage = models.PositiveInteger(default=0)

    def __str__(self):
        return f"{self.nom}"


class Livre(models.Model):
    titre = models.CharField(max_length=300)
    sous_titre = models.CharField(max_length=300, blank=True)
    slug = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    isbn_numerique = models.CharField(max_length=20, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    langue = models.CharField(max_length=20,default="français")
    date_publication = models.DateField(blank=True)
    note_moyenne = models.DecimalField(max_digits=3, decimal_places=2,default=0)
    nombre_ventes = models.PositiveIntegerField(default=0)

    class Statut(models.TextChoices):
        PUBLIE = 'publie', 'Livre Publié'
        BROUILLON = 'brouillon', 'Brouillon'
        ARCHIVE = 'archive', 'Une archive'
    status = models.CharField(max_length=10, choices=Statut.choices,default=Statut.PUBLIE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name="categorie", default="Roman")

    def __str__(self):
        return f"{self.titre} est un livre en {self.langue} au prix de {self.prix}"


    def afficher_tous_les_livres(self):
        livres = Livre.objects.all()
        return livres

    def afficher_livres_par_titre(self, titre, **filtres):
        pass


class FormatLivre(models.Model):
    class Format(models.TextChoices):
        PDF = "pdf", "Format PDF"
        EPUB = "epub", "Format EPUB"

    format = models.CharField(max_length=5, choices = Format.choices)
    chemin_fichier = models.URLField()
    taille_fichier_en_mo = models.DecimalField(max_digits=7, decimal_places=2)
    date_upload = models.DateTimeField(auto_now_add=True)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name="livre_format")

    def __str__(self):
        return f"{self.livre.titre} au format {self.format} de taille {self.taille_fichier_en_mo}"


class Auteur(models.Model):
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    biographie = models.TextField(blank=True)
    pays = models.CharField(blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
