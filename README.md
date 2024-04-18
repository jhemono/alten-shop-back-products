Une application de gestion d'un référentiel article.

Cette application est consitituée d'un front-end et d'un back-end dockerisés et orchestrés avec docker compose.

## Front-end

Le front-end est une application Angular. Attention, actuellement celle-ci ne communique pas avec le back-end mais fonctionne avec une source de données en mémoire. Elle est par ailleurs servie avec ng serve qui n'est pas destiné à la production.

L'image docker est product-trial-front:latest. Le service docker compose est "front" et il écoute sur le port 4200.

## Back-end

Ce service est basé sur Flask, Flask-RESTful, SQLAlchemy et Marshmallow. Les données sont stockées dans une base SQLite dans un volume docker. Gunicorn est utilisé comme serveur HTTP de production. Une documentation Swagger est rendue disponible sur http://localhost:5000/apidocs/.

L'image docker est product-trial-back:latest. Le service docker compose est "back" et il écoute sur le port 5000.

### Usage

Créer un article :
```term
$ curl --request POST \
  --url http://localhost:5000/products \
  --header 'content-type: application/json' \
  --data '{"code": "f230fh0g3","name": "Bamboo Watch","description": "A very technical watch.","image": "bamboo-watch.jpg","price": 65,"category": "Accessories","quantity": 24,"inventoryStatus": "INSTOCK"}'
```

Lister tous les articles :
```term
$ curl --request GET \
  --url http://localhost:5000/products
```

Obtenir un article :
```term
$ curl --request GET \
  --url http://localhost:5000/products/1
```

Modifier un article :
```term
$ curl --request PATCH \
  --url http://localhost:5000/products/1 \
  --header 'content-type: application/json' \
  --data '{"name": "Punk Bamboo Watch","rating": 4}'
```

Supprimer un article :
```term
$ curl --request DELETE \
  --url http://localhost:5000/products/1
```

## Utilisation

Les commandes suivantes s'exécutent depuis la racine du projet. (contenant le fichier docker-compose.yml)

Pour lancer le projet :
```term
$ docker compose up
```

Pour (re)construire les images :
```term
$ docker compose build
```

Pour gagner du temps, on peut ajouter le nom du service (back ou front) aux commandes précedentes.

Pour nettoyer (donnés persistantes comprises) :
```term
$ docker compose down -v
```

Pour rettoyer les images, supprimer toutes les images dont le nom commence par product-trial.
