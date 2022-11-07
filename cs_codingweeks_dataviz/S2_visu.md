# Fonctionnalité 5 : Visualisation des statistiques sur le corpus

Il s'agit ici d'afficher de manière visuelle les résultats de vos analyses sur le corpus. Pour ce MVP, on tirera partie de la bibliothèque `matplotlib` de python que vous avez déjà utilisée dans le cadre du cours de SIP.

Des tutoriaux sont disponibles:

+ [tutoriel 1](http://www.python-simple.com/python-matplotlib/matplotlib-intro.php)
+ [tutoriel 2](https://realpython.com/python-matplotlib-guide/) et [ici](https://realpython.com/courses/python-plotting-matplotlib/)
+ [tutoriel 3](https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/4740942-maitrisez-les-possibilites-offertes-par-matplotlib)

et bien sûr la documentation officielle [ici](https://matplotlib.org/tutorials/index.html).

Cette partie est libre. Vous pouvez la réaliser comme vous le souhaitez.
Il est attendu au minimum :

* une visualisation sous forme de camenbert du corpus montrant la répartition des opinions.
* une représentation sous la forme d'un histogramme et qui montre pour toutes les miss représentées dans le corpus leur nombre de tweets positifs ou négatifs.
* une représentation des opinions qualifiant une miss donnée. Par exemple, on pourrait imaginer un histogramme des différentes opinions associées à une miss, avec leur polarité (positif ou négatif). 
 
La première visualisation sera assez facile à faire. Pour la deuxième, il vous sera très certainement nécessaire de rajouter des fonctions et très certainement **ajouter un module `annotation_analysis`.** En effet, pour pouvoir construire la réprésentation, il faut déjà :

* Pour un tweet donné et l'annotation correspondante, déterminer si le sujet ou les sujets de l'annotation font référence à des Miss. 
* Pour un tweet donné, dire si il est positif ou négatif.
* ...

Cette étape nous montre que le découpage en sprints et en fonctionnalité de notre projet pourrait être revu, notamment pour ajouter une fonctionnalité d'analyse des annotations.



**Petit conseil**: pensez à  utiliser des [expressions régulières](https://docs.python.org/3/library/re.html) pour déterminer si un sujet traite d'une miss ou non. Un bon tutoriel concernant les expressions régulières est disponible [ici](http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_regex/regex.html). 


Il faudra bien documenter vos programmes, les tester et comme d'habitude faire les étapes nécessaires de gestion de votre version avec git et gitlab.


Maintenant, nos avons presque toutes les briques fonctionnelles du MVP. Il reste à permettre une éxécution facile de notre outil de visualisation, en permettant son paramètrage mais aussi son exécution facile.

Il s'agit du sprint 3 qui consiste à finaliser le MVP avec la  [**Fonctionnalité 6 : Un programme principal**](./S3_main.md)












