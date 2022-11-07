# Fonctionnalité 1 : Charger et afficher une image avec OpenCV

L'objectif de cette première partie est de prendre en main la bibliothèque [OpenCV](https://opencv.org/) qui est une des bibliothèques de référence en vision par ordinateur et qui est [open-source](https://sourceforge.net/projects/opencvlibrary/).
Nativement écrite en C, puis C++, elle a des interfaces en plusieurs languages dont python. Une documentation relativement complète d'OpenCV python est disponible [ici]( https://opencv24-python-tutorials.readthedocs.io/en/stable/).


## Etape 1 : Installer OpenCV

Pour installer OpenCV, il suffit d'executer l'une des commandes ci-dessous depuis un terminal :

` pip install opencv-contrib-python `

` python -m pip install opencv-contrib-python `

` python3 -m pip install opencv-contrib-python `

` py -m pip install opencv-contrib-python `

Sous réserve que l'utilitaire `pip` soit installé sur votre ordinateur ce qui devrait être le cas.

Pour tester la bonne installation d'OpenCV, ouvrer une console python (vous pouvez le faire en tapant la commande `python` depuis un terminal ou avec la commande `Python: Start REPL` accessible depuis la palette de commande de Visual Studio Code) et taper les commandes ci-dessous:

```
import cv2
print(cv2.__version__)
```

Si tout se passe bien, c'est que vous avez bien installé OpenCV. Si non, alors, essayez de trouver ce qui ne vas pas. Un guide complet autour de l'installation d'OpenCV est disponible [ici](https://www.pyimagesearch.com/opencv-tutorials-resources-guides/).


## Etape 2 : le Hello World de OpenCV

Dans cette étape nous allons utiliser OpenCV pour lire et pour afficher une image.
 
 + Ajouter un module `utils_cv` à votre projet. Pour rappel, il suffit d'ajouter un répertoire `utils_cv` à votre projet et d'y mettre un fichier `__init__.py`.
 + Créer un répertoire `Data` à la racine de votre projet et ajouter y l'[image](./Images/tetris_blocks.png) ci-dessous.

 ![Tetris](./Images/tetris_blocks.png)

Il s'agit maintenant d'écrire le code permettant de charger et d'afficher cette image. On définira pour cela la fonction `load_and_display_image(filename)` dans le module `load_data`. Il faudra pour cela utiliser les fonctions `imread()` et `imshow()` disponibles dans la bibliothèque OpenCV. Pour vous aider, vous pouvez regarder [cette partie](https://opencv24-python-tutorials.readthedocs.io/en/stable/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image) du tutorial d'OpenCV.

Tester votre fonction en l'utilisant pour afficher l'image `tetris_blocks.png`. 

Si vous n'y arrivez pas, vous pouvez regarder une solution [ici](./Codes/load_data.py).

Si l'image s'affiche correctement, vous avez maintenant terminé la fonctionnalité 1.


Avant de passer à la suite, nous allons introduire une approche de développement qui s'appelle le [**TDD (Test Driven Development)**](https://fr.wikipedia.org/wiki/Test_driven_development) qui consiste à spécifier le comportement attendu via un test avant de l’implémenter effectivement. Le principe est donc d'écrire en premier lieu le test et ensuite le code le plus simple possible qui permette au test de passer et donc de satisfaire le comportement spécifié. Le code peut ensuite être amélioré. L'idée est donc de se focaliser sur les fonctionnalités plutôt que sur le code.

Nous n'allons pas forcement utiliser massivement cette méthode lors de projet mais il est important de la connaître. Prenons donc une nouvelle fonctionnalité qui consiste uniquement à créer une image blanche (image en niveau de gris dont chaque pixel aura comme intensité la valeur 255). 


 1. **Critères d'acceptance.**

 Une des premières tâches à faire ici est de rechercher et de lister l'ensemble des critères qui permettront de répondre correctement aux besoins que la fonctionnalité *Créer une image blanche* est sensée couvrir. Ces critères sont des **critères d'acceptance**. Ici, c'est très simple, le critère d'acceptance de *Créer une image blanche* est d'**avoir un tableau numpy en deux dimensions dont chaque composante a pour valeur 255**. 
 

 
 2. **Developpement en mode TDD**

 Le **TDD (Test Driven Development)** est un développement dirigé par les tests et donc la première ligne de votre programme doit être dans un fichier de tests. Dans notre cas, nous utiliserons le module [`pytest`](https://docs.pytest.org/en/latest/) qu'il faut donc ajouter à votre projet. Vous pouvez aussi utiliser de la même manière `unittest` inclus dans la bibliothèque standard de python. Le principe du TDD repose sur 3 étapes complémentaires.
 
   + Première étape (**<span style='color:red'>RED</span>**) : Ecrire un premier test qui échoue.
   + Deuxième étape (**<span style='color:green'>GREEN</span>**) : Ecrire le code le plus simple qui permet de passer le code.
   + Troisième étape (**REFACTOR**) : Améliorer le code source.


Nous allons donc appliquer cette méthode à la fonctionnalité de création d'une image blanche (sans affichage de celle-ci) et de taille *4 x 4*. L'exemple est un exemple jouet pour vous montrer le principe du TDD. 

#### **<span style='color:red'> ETAPE RED</span>**

Notre premier test va consister à tester que lors de l'appel de la fonction `create_white_image` on dispose bien d'une image (array numpy) de taille *4 x4* et composée de pixels blancs. 

```PYTHON
from create_white_image import create_white_image
from pytest import *
import numpy as np


def test_create_white_image():
    assert np.array_equal(create_white_image(),np.array([[[255], [255], [255], [255]], [[255], [255], [255], [255]], [[255], [255], [255], [255]], [[255], [255], [255], [255]]], dtype=np.uint8)) == True



```

Recopier ce code dans un fichier `test_create_white_image.py`.
Ce test doit échouer, puisqu'en l'état actuel du projet, le code pour `create_white_image` n'existe pas et on a donc l'erreur suivante lors de l'exécution du code <span style='color:red'>`ImportError: cannot import name 'create_white_image'`<span>

#### **<span style='color:green'> ETAPE GREEN</span>**

On va maintenant écrire le code qui permet de faire passer ce test le plus rapidement possible.

Il suffit pour cela de :

+ Créer le fichier `create_white_image.py` dans le package `utils_cv`.
+ Créer et compléter une fonction `create_white_image` dans le fichier `create_white_image.py` de telle manière que le test précédent passe.

 On pourra par exemple, définir la fonction ci-dessous dans le fichier `create_white_image.py`
 
```PYTHON
import numpy as np
import cv2


def create_white_image():
    a = 255*np.ones(shape=[4, 4, 1], dtype=np.uint8)
    return a



```
 
 Votre test devrait passer au vert avec cette **<span style='color:green'> ETAPE GREEN</span>**
 

#### **<span style='color:black'> ETAPE REFACTOR</span>**
   
La dernière étape consiste en une étape de [refactoring](https://refactoring.com/), à mettre en place si nécessaire.   

Le [refactoring](https://en.wikipedia.org/wiki/Code_refactoring) (ou réusinage de code) est un principe de programmation qui consiste à changer la structure interne d’un logiciel sans en changer son comportement observable. C'est une étape qui doit toujours être exécutée quand les différents tests sont au vert et qui n'est pas obligatoire. Elle doit surtout permettre d'améliorer la **qualité du code** par exemple en améliorant :
 
 + **la conception** : decoupage en fonctions, modules ou classes afin de rendre votre code le plus simple possible.
 + **la lisibilité du code** : il faut ici prendre le temps d'appliquer les principes du [clean code](https://cleancoders.com/cart) introduit par Robert C. Martin dans l'ouvrage du même nom et dont un des principe est celui des boy-scouts (*« The Boy Scout Rule »*): *« Toujours laisser un endroit dans un état meilleur que celui où vous l’avez trouvé »*.
 
Dans notre cas, une des premiers principes est de vérifier du bon nommage (variables, fonctions, packages, classes et cie) et de la présence de commentaires dans notre code. 
 
 Vous trouverez [ici](https://github.com/zedr/clean-code-python#objects-and-data-structures) quelques principes du clean code transposé au langage python. Prenez le temps de lire rapidement ce site et appliquer ces différents principes au code que vous allez écrire.
 
Dans cette étape **<span style='color:black'> ETAPE REFACTOR</span>**, on peut aussi travailler à l'optimisation des performances du programme si cela s'avère vraiment nécessaire.
 
 
Dans notre cas, on peut par exemple procéder à une étape de renommage sur la variable `a`. En effet, il peut par exemple être plus explicite de nommer cette variable `white_image` ou `white_img`. Pour réaliser cette étape de renommage, il est fortement conseillé d'utiliser les fonctionnalités de Refactoring de votre editeur. En effet, ici cela ne vous semble peut être pas très utile mais avec un code plus complexe, ce sera très utile. Une documentation de comment Visual Studio Code peut être utilisé dans ce contexte est disponible [ici](https://code.visualstudio.com/docs/editor/refactoring)

Dans un souci de généricité, on peut aussi choisir de definir la taille de l'image comme un paramétre de notre fonction `create_white_image`. Il faudra bien modifier le code et le code de test en conséquence.



#### :white_check_mark: <span style="color: #26B260">A ce stade du projet, vous avez atteint le JALON 3 : Ecrire du code dans une démarche TDD </span> 




#### **ATTENTION**

1. **Après cette étape, n'oubliez pas de relancer les tests pour vérifier que le comportement de votre code n'a pas changé et que tout est encore bien AU VERT !**

2. On vient ici de terminer la réalisation de l'étape *Charger et créer une image* et il convient donc de **committer ce changement dans votre gestionnaire de version avec un message de commit explicite reprenant l'objectif de l'étape**. Pensez aussi à mettre à jour votre dépôt distant.


Comme nous venons de terminer une fonctionnalité,

#### :white_check_mark: <span style="color: #26B260">A ce stade du projet, vous avez atteint le JALON 4 : une première vraie utilisation de git et gitlab avec mon groupe projet </span> 










## A propos de la gestion des versions

<span style='color:blue'> Pour toute la suite du projet, il vous est demandé de :</span> 

+ <span style='color:blue'>Faire un commit dès que la réalisation d'une fonctionnalité ou d'une sous-fonctionnalité est finie.</span> 
+ <span style='color:blue'>Tagger à la fin de chaque journée votre dernier commit </span> 
+ <span style='color:blue'>De faire une revue de code au sein de l'équipe pour chaque fonctionnalité.</span>
+ <span style='color:blue'>De mettre le code stable sur la branche `master`.</span>
+ <span style='color:blue'>Pousser (Push) le code vers votre dépôt distant sur GitLab.</span> 


Après avoir mis à jour votre dépôt git local et distant, vous pouvez maintenant passer à la [**Fonctionnalité 2** : Effectuer un traitement sur une image et afficher le résultat du traitement.](./Facerecognition_S1_traitement.md)









