# Fonctionnalité 1 : Prise en main du corpus Canephore


Pour ce projet, nous allons travailler avec un corpus de tweets en Français, le corpus [Canephore](https://github.com/ressources-tal/canephore).

Ce corpus est un corpus de tweets annotés pour l'évaluation de la fouille d'opinion ciblée. Il nous permettra de construire notre MVP sans avoir à mettre en place une stratégie de collecte de tweets sur Twitter et il servira aussi à apprendre un modèle de prédiction d'opinions adapté aux tweets en français.

Votre premier travail consiste donc à regarder et à comprendre ce corpus en le récupérant [ici](https://github.com/ressources-tal/canephore) et en lisant l'article scientifique associé [ici](https://hal.archives-ouvertes.fr/hal-01169293).

Comme pour tout corpus de tweets, à cause de la politique de confidentialité mise en place par Twitter, il est juste composé d'un ensemble d'identifiants de tweets et des annotations d'opinions associées. Pour pouvoir travailler sur les données elles-mêmes, il est donc nécessaire de récupérer les tweets associés aux identifiants.

Pour cela, une fonction est proposée sur le dépôt du jeu de données, la fonction `retrieve-tweets.py`. Il est d'ailleurs intéressant d'observer que le `README` de ce dépôt explique bien le contenu du dépôt et comment utiliser ce code. C'est un bon exemple et typiquement, à la fin de cette première semaine, le dépôt gitlab de votre projet devra aussi permettre cela.

Un premier travail de programmation intéressant pourrait donc consister à comprendre et à réutiliser un code existant donné dans le fichier `retrieve-tweets.py`. 

Cela pourrait correspondre au <span style="color: #26B260"> JALON supplémentaire : je sais récupérer un projet de développement existant et le faire fonctionner </span> .

Cependant, votre lecture du code doit vous montrer que, pour utiliser ce code, il faut aussi pouvoir faire des requêtes à l'API Twitter et donc avoir un compte développeur, ce qui peut être une étape longue. Il faudrait typiquement faire l'ensemble des instructions décrites dans [cette étape](./S1_twitterconnect.md).

Comme nous cherchons à construire un MVP rapidement et comme le coeur de notre produit est l'analyse et la visualisation et non pas la collecte, ce n'est clairement pas une fonctionnalité prioritaire. 


Pour vous permettre de travailler, les tweets encore accessibles du corpus ont été récupérés pour vous et vous pouvez donc télécharger le dossier les contenant [ici](https://filesender.renater.fr/?s=download&token=e018677c-67d5-4406-ab5c-a155ab5aadeb).


Une fois le corpus récupéré, il faut associer les données à votre projet `datavisualization`. Créez un répertoire `Data` à la racine de votre projet et mettez-y les données téléchargées.


Cette étape peut d'ailleurs une étape intéressante pour réfléchir à la structure du code de votre projet. Combien de modules et packages par exemple ?


Pour pouvoir utiliser les annotations, il est nécéssaire aussi de comprendre le format des annotations qui respecte le standard de Brat décrit [ici](http://brat.nlplab.org/standoff.html). **Prenez bien le temps de lire ce document pour pouvoir récupérer ensuite l'information intéressante dans ces annotations.**





Nous avons fini ici la fonctionnalité 1. Il n'y a pas vraiment eu d'écriture de code dans cette fonctionnalité mais plutôt de la récupération de données. Cependant, vous avez normalement ajouté à votre projet un répertoire `Data` avec les tweets récupérés.

Une question importante à se poser ici est le statut de ces fichiers par rapport à votre dépôt git et son clone sur gitlab. Ici, pour plusieurs raisons dont la principale est leur confidentialité, il n'est pas souhaitable d'ajouter les tweets à notre dépôt. Il est d'ailleurs illégal de mettre ces données sur un repo gitlab publique.

On va donc indiquer ici à git qu'il faut ignorer ces données. Pour cela, on va associer à la racine de notre dépôt un fichier `.gitignore`.

Ce fichier contiendra ce type d’information :

```
# Les ligne commençant par '#' sont des commentaires.
# Ignorer tous les fichiers nommés foo.txt
foo.txt
# Ignorer tous les fichiers html
*.html
# à l'exception de foo.html qui est maintenu à la main
!foo.html
# Ignorer les objets et les archives
*.[oa]
```


Ecrire le fichier `.gitignore` à la racine de votre dépôt et compléter le de manière à ignorer le répertoire `Data`.


Vous pouvez maintenant passer à la [**Fonctionnalité 2** : Un utilitaire d'accès aux données.](./S1_canephoredataacess.md)






