# Simulation du pendule simple - Sprint 0 : Reflexion autour de la conception

Après cette phase d'analyse, nous pouvons avoir une première démarche de conception et essayer d'identifier les principaux objets de notre MVP. 

En lisant la [description du pendule simple sur Wikipedia](https://fr.wikipedia.org/wiki/Pendule_simple), on identifie notamment un certain nombre de concepts comme ceux de **pendule**, **vitesse**, **masse**, **position**, **énergie mécanique**, **oscillation**, ainsi que tous les concepts faisant référence au phénomène physique dont on souhaite oberver le comportement. 


## Vers un langage commun

Dans cette phase de reflexion sur la conception, pour favoriser le travail collaboratif et une compréhension commune entre tous les membres du projet, il est important de définir, dès le début du projet, un **vocabulaire commun** autour des termes métier. Dans le jargon du développement logiciel, on parle de [**ubiquitous language**](http://referentiel.institut-agile.fr/ubiquitous.html) ou **langage omniprésent**. C'est un principe issu de l'approche *Domain Driven Design* décrite dans l'[ouvrage](https://github.com/p0w34007/ebooks/blob/master/Eric%20Evans%202003%20-%20Domain-Driven%20Design%20-%20Tackling%20Complexity%20in%20the%20Heart%20of%20Software.pdf) du même nom et qui consiste à identifier et à définir un langage commun autour des termes métiers.


Dans le cas de la simulation du pendule, c'est un travail qui peut vous sembler fastidieux et très certainement inutile mais qui vous sera très utile pour de nombreux autres projets, impliquant différents acteurs.

Le déroulé de cette approche consiste à produire ce que l'on appelle des [**User Stories**](https://en.wikipedia.org/wiki/User_story) (avec l'ensemble des parties prenantes du projet) qui représentent les besoins des utilisateurs à implémenter. Ce travail permet aussi de définir le langage partagé.

Une **user story** ce n'est rien d'autre qu'une phrase simple, en language naturel, qui permet de décrire le contenu d'une fonctionnalité à développer en précisant le *Qui?*, le *Quoi?* et le *Pourquoi?*

 `En tant que <qui>, je veux <quoi> afin de <pourquoi>`

Ici, typiquement, selon l'objectif souhaité, on pourrait avoir les stories suivantes : 

+ En tant qu'utilisateur de l'application , je veux pouvoir **paramétrer la simulation du mouvement** du pendule
+ En tant qu'utilisateur de l'application , je veux pouvoir **paramétrer le modèle** du pendule lui-même.
+ En tant qu'utilisateur de l'application, je veux pouvoir **être alerté** lors de l'observation d'un phénomène intéressant.
+ En tant qu'enseignant, je veux pouvoir **générer, paramétrer et sauvegarder des animations** de simulation du pendule.
+ ...

L'objectif de cette phase est principalement de réflechir à la finalité de l'application que l'on développe et à son appropriation par les utilisateurs visés.


Concernant le langage partagé, dans le cas du pendule, plusieurs termes sont utilisés pour parler de la tige par exemple : *fil*, *tige*,.... Le concept même de pendule simple pourrait avoir besoin d'être défini.

Il est donc nécessaire de choisir un terme précis pour chaque objet de l'application. 


## Les principaux objets, modules de votre application

Cette phase d'analyse doit aussi vous faire réflechir à la conception de votre application et notamment aux différents objets et modules de cette dernière en essayant de séparer les responsabilités. 

Pour cela, essayez de réflechir à l'architecture fonctionnelle de votre application et à comment les différents acteurs, modules, objets intéragissent entre eux. Faites le avec un papier et un crayon, de manière schématique. Un travail et une reflexion de groupe peuvent être intéressantes ici !

Prenez un peu de temps pour faire ce travail. Une fois terminé, prenez une photo de ce que vous avez mis sur papier et stockez cela dans un répertoire intitulé `WorkingDocs`de votre dépôt git. N'oubliez pas de faire un `commit` et de mettre à jour votre dépôt distant.

 
L'objectif de ce travail est de vous permettre de modéliser, du point de vue informatique, votre problème mais il est essentiel aussi pour l'organisation de votre travail, c'est-à-dire, son découpage en différents sprints et fonctionnalités par exemple. 

Ici, ce travail a été fait partiellement pour vous mais, il faudra le faire pour votre projet de la semaine 2.

#### <span style="color: #26B260"> :white_check_mark: A ce stade du projet, vous avez atteint le JALON 2 : Analyse et Conception de mon produit </span> 

Vous pouvez maintenant passer à la [**Fonctionnalité 1** : représentation d'un pendule.](./pendulum_S1_pendule.md)