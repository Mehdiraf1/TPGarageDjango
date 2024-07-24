# TPGarageDjango
Gestion d'un garage en Django

# Prérequis
Installer les requirements avec pip install requirements

Cela comprend les librairies suivantes : 

- Django
- Django REST Framework
- DRF Simple JWT (optionnel)
- MySQL Client

# Cloner le projet

git clone https://github.com/Mehdiraf1/TPGarageDjango.git

# Se connecter à la base de données

- Nom de de la BD : Garage_Django
- Nom d'utilisateur : root
- Mot de passe : Mehdiraf10*
- Host : localhost
- Port : 3306

# Gestion des utilisateurs / roles

Vous pouvez ajouter des utilisateurs et leur assigner les rôles suivants :

- Réceptionniste :
  - Droit :
      - Peut voir les voitures
      - Peut ajouter des voitures
      - Peut modifier ou supprimer les voitures qu'il a ajoutées

- Mécanicien :
  - Droit :
      - Peut voir les voitures
      - Peut changer l'état des voitures

- Client :
  - Droit :
      - Peut voir les voitures
