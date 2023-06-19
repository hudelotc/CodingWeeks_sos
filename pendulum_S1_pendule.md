# Fonctionnalité 1 : Modélisation du pendule



L'objectif de cette première fonctionnalité est de pouvoir **modéliser l'objet principal de la simulation**, c'est-à-dire le **pendule** lui même. 

Il s'agira donc de :

+ Demander à l'utilisateur de choisir les paramètres du pendule : sa masse, la longueur de la tige,....
+ D'écrire le programme permettant de générer un modèle du pendule voulu.



Nous allons ici nous familiariser avec l'approche de développement [**TDD (Test Driven Development)**](https://fr.wikipedia.org/wiki/Test_driven_development) qui consiste à spécifier le comportement attendu via un test avant de l’implémenter effectivement. Le principe est donc d'écrire en premier lieu le test et ensuite le code le plus simple possible qui permette au test de passer et donc de satisfaire le comportement spécifié. Le code peut ensuite être amélioré. L'idée est donc de se focaliser sur les fonctionnalités plutôt que sur le code.

Nous allons d'abord travailler pas à pas puis vous prendrez au fur et à mesure de l'autonomie sur cette approche. 

## Créer un pendule

Pour créer le pendule, il faut identifier les données qu'il faudra manipuler, c'est-à-dire les données nécéssaires pour représenter l'objet pendule. Puis, il s'agira ensuite de choisir les structures de données, dans le sens informatique, à utiliser.

 1. **Critères d'acceptance.**

 Une des premières tâches à faire ici est de rechercher et de lister l'ensemble des critères qui permettront de répondre correctement aux besoins que la fonctionnalité *Créer un pendule* est sensée couvrir. Ces critères sont des **critères d'acceptance**. Ici, c'est très simple, le critère d'acceptance de *Créer un pendule* est d'**avoir une représentation informatique d'un pendule** nous permettant d'agir dessus, c'est-à-dire un objet composé d'une extrémité, d'une masse, d'une tige définie par sa longueur, d'une orientation initiale.
 
 
 
 2. **Développement en mode TDD**

 Le **TDD (Test Driven Development)** est un développement dirigé par les tests et donc la première ligne de votre programme doit être dans un fichier de tests. Dans notre cas, nous utiliserons le module [`pytest`](https://docs.pytest.org/en/latest/) qu'il faut donc ajouter à votre projet. Le principe du TDD repose sur 3 étapes complémentaires.
 
   + Première étape (**<span style='color:red'>RED</span>**) : Ecrire un premier test qui échoue.
   + Deuxième étape (**<span style='color:green'>GREEN</span>**) : Ecrire le code le plus simple qui permet de passer le code.
   + Troisième étape (**REFACTOR**) : Améliorer le code source.


Nous allons donc appliquer cette méthode à la fonctionnalité de la création du pendule.

#### **<span style='color:red'> ETAPE RED</span>**

Notre premier test va consister à tester que étant donné une masse, une taille et une orientation voulue, notre pendule a bien été construit.

```PYTHON
from create_pendulum import *
from pytest import *

def test_create_pendulum():
    assert create_pendulum(10,10,10) == (10,10,10)
```

Recopiez ce code dans un fichier `test_create_pendulum.py`.
Ce test doit échouer, puisqu'en l'état actuel du projet, le code pour la fonction et même le module `create_pendulum` n'existe pas et on a donc l'erreur suivante lors de l'exécution du code <span style='color:red'>`ImportError: cannot import name 'create_pendulum'`<span>

#### **<span style='color:green'> ETAPE GREEN</span>**

On va maintenant écrire le code qui permet de faire passer ce test le plus rapidement possible.

Il suffit pour cela de :

 + Créer le fichier `create_pendulum.py` dans le projet.
 + Créer et compléter une fonction `create_pendulum` dans le fichier `create_pendulum.py` de telle manière que le test précédent passe.

 On pourra, par exemple, définir la fonction ci-dessous dans le fichier `create_pendulum.py`
 
```PYTHON
def create_pendulum(a,b,c):
    a = a
    b= b
    c = c
    return (a,b,c)
    
```
 
 Votre test devrait passer au vert avec cette étape:  **<span style='color:green'> ETAPE GREEN</span>**
 
 <img src="./Images/pytestpendulum.png" alt="drawing" width="600"/>
 
 
 

#### **<span style='color:black'> ETAPE REFACTOR</span>**
   
La dernière étape consiste en une étape de [refactoring](https://refactoring.com/), à mettre en place si nécessaire.   

Le [refactoring](https://en.wikipedia.org/wiki/Code_refactoring)(ou réusinage de code) est un principe de programmation qui consiste à changer la structure interne d’un logiciel sans en changer son comportement observable. C'est une étape qui doit toujours être exécutée quand les différents tests sont au vert et qui n'est pas obligatoire. Elle doit surtout permettre d'améliorer la **qualité du code** par exemple en améliorant :
 
 + **la conception** : decoupage en fonctions, modules ou classes afin de rendre votre code le plus simple possible.
 + **la lisibilité du code** : il faut ici prendre le temps d'appliquer les principes du [clean code](https://cleancoders.com/cart) introduit par Robert C. Martin dans l'ouvrage du même nom et dont un des principes est celui des boy-scouts (*« The Boy Scout Rule »*): *« Toujours laisser un endroit dans un état meilleur que celui où vous l’avez trouvé »*.
 
Dans notre cas, une des premiers principes est de vérifier du bon nommage (variables, fonctions, packages, classes et cie) et de la présence de commentaires dans notre code. 
 
 Vous trouverez [ici](https://github.com/zedr/clean-code-python#objects-and-data-structures) quelques principes du clean code transposé au langage python. Prenez le temps de lire rapidement ce site et appliquer ces différents principes au code que vous allez écrire.
 
Dans cette étape **<span style='color:black'> ETAPE REFACTOR</span>**, on peut aussi travailler à l'optimisation des performances du programme si cela s'avère vraiment nécessaire.
 
 
Dans notre cas, on peut par exemple procéder à une étape de renommage sur la variable `a`. En effet, il peut par exemple être plus explicite de nommer cette variable `mass`. De même `b` pourrait être renommée en `length` et `c` en `initial_orientation`.  Pour réaliser cette étape de renommage, il est fortement conseillé d'utiliser les fonctionnalités de Refactoring de votre IDE. En effet, ici cela ne vous semble peut être pas très utile mais avec un code plus complexe, ce sera très utile. Prenez le temps de lire les propriétés de Visual Studio Code dans ce contexte [ici](https://code.visualstudio.com/docs/editor/refactoring)


On peut aussi ici se poser la question du choix de la structure de données utilisée pour représenter le pendule. En effet nous voulons pouvoir accéder facilement aux différentes propriétés d'un pendule et nous aimerions aussi pouvoir éventuellement faire évoluer cette représentation.
En programmation orientée objet, une approche aurait pu consister en la repésentation du pendule par une classe. Pour éviter d'avoir à utiliser la programmation objet, nous représenterons donc ici un pendule par un dictionnaire.

Modifier donc votre code (et les tests associés) pour représenter un pendule comme un dictionnaire python (`dict`).

```PYTHON
def create_pendulum(mass,length,orientation):
    pendulum= {}
    pendulum["mass"] = mass
    pendulum["length"] = length
    pendulum["initial_orientation"] = orientation
    return pendulum
    
```



**Faites ce travail de refactoring** et vous aurez ainsi terminé la fonctionnalité 1.


#### <span style="color: #26B260"> :white_check_mark: A ce stade du projet, vous avez atteint le JALON 3 : Ecrire du code dans une démarche TDD </span> 



**<span style='color:blue'>Commiter maintenant vos changements dans votre gestionnaire de version. C'est aussi le moment de faire la mise en commun et la revue de code avec les autres membres de votre équipe.</span>**


#### <span style="color: #26B260"> :white_check_mark: A ce stade du projet, vous avez atteint le JALON 4 : une première vraie utilisation de git et gitlab avec mon groupe projet </span> 



## A propos de la couverture de code par vos tests

Une couverture de code par les tests (code coverage) nous permet de connaître le pourcentage de notre code qui est testé et donc cela permet d'avoir une idée de ce qui reste d'ombre dans notre projet.

En règle générale, on considère qu'une couverture de code supérieure à 80% est signe d'un projet bien testé et auquel il sera alors plus facile de rajouter de nouvelles fonctionnalités.

Pour connaitre le taux de couverture de votre projet, vous pouvez utiliser des bibliothèques python [`coverage`] et [`pytest_cov`] qu'il faut donc installer soit en ligne de commande soit depuis votre IDE.

`pip3 install coverage`

`pip3 install pytest-cov`

Il faut ensuite vous placer dans le répertoire de votre projet et lancer la commande suivante :

`pytest --cov=pendulum --cov-report html test_*.py`

Cette commande permet de tester les fichiers contenus dans le dossier 'pendulum', crée un rapport en html et le place dans le répertoire `htmlcov` et utilise les tests qui sont dans ce répertoire et qui sont de la forme `test_[caracteres].py`.

L'ouverture du fichier `index.html`dans le répertoire `htmlcov`vous permet de visualiser un bilan du test de couverture qui devrait être bon dans la mesure où vous avez utilisé l'approche TDD. Un clic sur chacun des fichiers permet aussi d'avoir un bilan propre à chaque fichier.

Les illustrations ci-dessous donnent l'exemple de ce que l'on obtient pour un autre projet.

![testcoverage](./Images/coverage.png)



![testcoverage](./Images/coveragebis.png)


#### <span style="color: #26B260"> :white_check_mark:  A ce stade du projet, vous avez atteint le JALON 5 : une première couverture de mon projet par des tests </span> 



## A propos de la gestion des versions

<span style='color:blue'> Pour toute la suite du projet, il vous est demandé de :</span> 

+ <span style='color:blue'>Faire un commit dès que la réalisation d'une fonctionnalité ou d'une sous-fonctionnalité est finie.</span> 
+ <span style='color:blue'>Tagger à la fin de chaque journée votre dernier commit </span> 
+ <span style='color:blue'>De faire une revue de code au sein de l'équipe pour chaque fonctionnalité.</span>
+ <span style='color:blue'>De mettre le code stable sur la branche `master`.</span>
+ <span style='color:blue'>Pousser (Push) le code vers votre dépôt distant sur GitLab.</span> 
+ <span style='color:blue'>Faire un test de couverture de code à la fin de chaque journée et de pousser le bilan obtenu vers votre dépôt distant sur GitLab.</span>





Vous pouvez maintenant passer à la [**Fonctionnalité 2 : Afficher et visualiser le pendule**](./pendule_S1_visualisation.md)





