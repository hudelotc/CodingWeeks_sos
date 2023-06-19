# Fonctionnalité 6 : Prise en main du module `argparse`

Il s'agit ici de permettre à un utilisateur de pouvoir choisir en ligne de commande les paramètres de la simulation comme :

+ la longueur du pendule,
+ la gravité,
+ la position initiale du pendule.



Pour cela, nous allons utiliser le module `argparse`de python. Des documentations de ce module sont disponibles ici :

 + Documentation officielle [ici](https://docs.python.org/3.8/library/argparse.html?highlight=argparse#module-argparse)
 + Tutorial RealPython [ici](https://realpython.com/command-line-interfaces-python-argparse/)

Formez vous rapidement à ce module!

Pour prendre en main ce module vous allez déjà permettre à l'utilisateur de choisir la longueur du pendule.

Pour cela, il faudra ajouter un module `launch_simulation_pendulum` dans le package pendulum qui sera appelé en ligne de commande de la manière suivante :

```
python launch_simulation_pendulum.py -h
OU
python launch_simulation_pendulum.py--help
OU
python launch_simulation_pendulum.py -l length 
OU
python launch_simulation_pendulum.py --length length 
```

L'appel de ce programme :

 + génèrera un pendule de la taille demandée,
 + simulera le mouvement de ce pendule avec les utilitaires développpées précédemment,
 + lancera une visualisation du mouvement du pendule sous la forme d'une animation `matplotlib`.


#### <span style="color: #26B260"> :white_check_mark: A ce stade du projet, vous avez atteint le JALON 7 : gérer les paramètres d'un programme en ligne de commande</span> 


 
Quand vous avez terminé et testé cette fonctionnalité, **n'oubliez pas de mettre à jour votre dépôt local et distant.**

Vous pouvez passer à la [**Fonctionnalité 7** : Un programme principal](./S4_gamemain.md) 



