# Fonctionnalité 4: Une première animation avec matplotlib


Nous voulons ici permettre de visualiser la simulation du mouvement du pendule. Pour l'affichage du pendule sans mouvement, nous nous sommes basés sur `matplotlib` et nous allons donc voir comment nous pouvons générer des animations avec cette bibliothèque.


## Etape 1 : Vous former aux fonctionnalités d'animation de matplotlib

L'affichage de votre pendule s'est, pour le moment, basé sur la bibliothèque `matplotlib`. Nous voulons maintenant pouvoir afficher une animation montrant le pendule en mouvement.

Vous ne savez pas comment faire ? Commencez par regarder si les outils à votre disposition, en l'occurence `matplotlib` permet de le faire.

En l'occurence, `matplotlib` possède un utilitaire d'animation décrit [ici](https://matplotlib.org/2.0.0/api/animation_api.html).

Votre premier travail est donc de vous former à cet utilitaire. Vous pouvez pour cela utiliser la documentation officielle [ici](https://matplotlib.org/2.0.0/api/animation_api.html) qui donne de nombreux exemples ou chercher d'autres tutoriaux. Cela ne manque pas :

+ [https://www.courspython.com/animation-matplotlib.html](https://www.courspython.com/animation-matplotlib.html)
+ [https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/](https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/)
+ [https://brushingupscience.com/2016/06/21/matplotlib-animations-the-easy-way/](https://brushingupscience.com/2016/06/21/matplotlib-animations-the-easy-way/)

Prenez le temps de lire et surtout de **tester** les possibilités de `matplotlib` pour comprendre comment cela fonctionne.




## Etape 2 : Une fonction pour voir l'évolution de l'univers

A partir de ce que vous avez appris dans l'étape précédente, écrire une fonction permettant de visualiser le mouvement simulé du pendule avec `matplotlib`. Vous pouvez par exemple regarder [cet exemple](https://matplotlib.org/3.1.1/gallery/animation/double_pendulum_sgskip.html), très proche de notre problème.

## Etape 3 : Sauver votre animation sous la forme d'un fichier vidéo.

La dernière étape consiste juste à sauvegarder votre animation sous la forme d'un fichier vidéo.


**N'oubliez pas de mettre à jour votre dépôt local et distant.** 


Vous pouvez passer à la [**Fonctionnalité 5** : visualisation du mouvement et de la vitesse du pendule au cours du temps](./S2_motionvisualisation.md)

