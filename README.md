# Projet de gestionnaire de tounrois d'échec

Centre Échecs est une application hors ligne développée en Python pour la gestion des joueurs et des tournois d'échecs.
Ce programme autonome permet d'ajouter des joueurs, de gérer des tournois, de suivre les résultats et de générer des rapports

## Fonctionnalités Principales: 

L'application est composée de 3 categories accesibles via le menu principal

### Gestion des Joueurs

**Choix 1. Creer des joueurs**

Permet l'ajout de joueurs au fichier des joueurs disponibles.

L'utilisateur pourra rentrer les informations concernant le joueur à ajouter.

* Nom de famille
* Prénom
* Date de naissance
* Identifiant national d’échecs (unique, format : XX12345)

Une fois les information rentrées le joueur est ajouté à la liste des joueurs dans le fichier JSON correspondant et le fichier est sauvegardé.

### Gestion des Tournois
**Choix 2. Tournois**

Déroulement d'un tournois:

1. L'utilisateur commence par créer ou charger un tournois (vois plus loin "Sauvegarde et chargement")
2. L'utilisateur ajoute des joueurs au tournois
    * Depuis la liste des joueurs existant
    * Grace à l'identifiant national d’échecs du joueur
    * En créant un nouveau joueur
3. Un fois le tournois crée ou chargé et les joueurs ajouté au tournois l'utilisateur lance le tournois

Le tournois peut etre interrompu et repris rechargé à tous moment. (vois plus loin "Sauvegarde et chargement")

### Rapports
**Choix 3. Rapports**

L'utilisateur peut acceder à diiferents par via ce menu:

* Liste de tous les joueurs par ordre alphabétique.
* Liste de tous les tournois.
* Détails d’un tournoi (nom, dates, joueurs, tours, matchs).

### Sauvegarde et Chargement

Le tournois en cours est sauvegardé automatiquament apres chaque changement. (Création du tounois, ajout de joueur, nouveau match, round, ...)

L'utilisateur peut charger un tournois depuis le menu tournois grace à l'option **1. Charger un tournois**

Le tournois pourra alors etre repris grace à l'option **"**4. Lancer/reprendre le tournois**"**

## Installation et utilisation

### Prérequis

* Python 3.x
* Dépendances : listées dans le fichier requirements.txt

Vous pouvez installer les dépendances nécessaires en utilisant la commande suivante en bash:
```
pip install -r requirements.txt
```

### Utilisation

Pour lancer le logiciel:
```
python superchess.py
```

### Résultats :

Le script va créer deux repertoires dans le repertoire data

* players: 
* tournament: 

## Structure du Projet

Le projet suit le modèle MVC (Modèle-Vue-Contrôleur) pour assurer la lisibilité et la maintenabilité :

* models : Définit les classes pour les joueurs, tournois, tours et matchs.
* views : Gère les interactions avec l'utilisateur via la console.
* controllers : Contient la logique métier et coordonne les actions entre les modèles et les vues.
* main.py : Point d'entrée principal du programme.



