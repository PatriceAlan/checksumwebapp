# API Flask pour les Checksums avec Redis

Ce projet est une API simple en Flask permettant de calculer des checksums (hachages) pour des chaînes de caractères en utilisant différents algorithmes de hachage (SHA-256, MD5, SHA-1). Les checksums sont stockés dans une base de données Redis et peuvent être récupérés ultérieurement.

## Fonctionnalités
- **Calcul de Checksum** : Accepte une chaîne d'entrée et calcule son checksum en utilisant SHA-256, MD5 ou SHA-1.
- **Stockage Redis** : Stocke les checksums calculés avec la chaîne d'entrée et l'algorithme sélectionné dans une base de données Redis.
- **Récupération des Checksums** : Un point de terminaison GET qui permet de récupérer tous les checksums stockés.

## Prérequis
- Docker
- Docker Compose

## Structure du Projet

- `app.py`: L'application principale Flask qui gère les requêtes.
- `index.html`: Un fichier HTML simple servi à l'endpoint racine.
- `Dockerfile`: Le fichier Dockerfile pour construire le service backend.
- `docker-compose.yml`: Fichier Docker Compose pour exécuter à la fois l'application Flask et le service Redis.
- `requirements.txt`: Liste des dépendances de l'application Flask.

## Installation

### Avec Docker

1. Clonez ce repository :
   ```bash
   git clone https://github.com/PatriceAlan/checksumwebapp.git
   cd checksumwebapp
   ```
Construisez et lancez les services avec Docker Compose :

```bash
docker-compose up --build
```
L'API sera disponible à l'adresse suivante : http://localhost:5000.

Dépendances
Assurez-vous d'installer les dépendances avant d'exécuter l'application en local :

Créez un environnement virtuel :

```bash
Copy code
python3 -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```
### Installez les dépendances :

```bash
pip install -r requirements.txt
```

L'API sera accessible à http://localhost:5000.
