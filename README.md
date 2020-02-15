
# Api pour la décompostion en nombres premiers d'un nombre entier
## Déploiement

Sur ubuntu, installez docker-compose

	sudo apt-get install docker-compose

à la racine du projet, créez une image docker de l'API

	sudo docker-compose build

Ensuite, exécutez l'image ainsi créée

	sudo docker-compose up

## Exécution

Nous pouvons maintenant accéder à l'API à partir de l'URL

	URL
	http://localhost:5000/factors/<nombre>

Exemple :

	http://localhost:5000/factors/28

	{"Nombre": "28", "Facteurs_premiers": [2, 2, 7]}

## Prise en compte du temps de calcul et de la montée en charge

Pour garantir de bonnes performances de l'api, nous avons déployé l'api en utilisant Nginx et uWSGI qui permettent

    - nginx est un serveur web et un reverse proxy utilisé ici pour le loadbalancing
    - uWSGI est un serveur WSGI (Web Server Gateway Interface) permettant le multithreading 

## Référence: 
A Guide to Scaling Machine Learning Models in Production
https://hackernoon.com/a-guide-to-scaling-machine-learning-models-in-production-aa8831163846


