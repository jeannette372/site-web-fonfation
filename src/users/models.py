from django.contrib.auth.models import AbstractUser
from django.db import models

# Ici il s'agit de tout ce qui a un lien avec les utilisateurs
"""
Cette classe gère les utilsateurs de lapplication


Le nom d'utilisateur : username 
Le nom de l'individu : last_name
Le prénom de l'individu : first_name
Le mot de passe : password
L'adresse mail : email
La date de la première connexion : date_joined


"""
class Utilisateur(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = 'client', 'CLIENT'
        ADMIN = 'admin', 'ADMIN'

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CLIENT)
    email_verifie = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} crée le {self.date_joined}"