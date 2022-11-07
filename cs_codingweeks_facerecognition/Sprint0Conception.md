# Facerecognition - Sprint 0 : Réflexion autour de la conception

Après cette phase d'analyse, nous pouvons avoir une première démarche de conception et essayer d'identifier les principaux *objets* de notre MVP. 

La question à se poser c'est *De quoi parle t'on ?* 

## Vers un langage commun

Dans cette phase de réflexion sur la conception, pour favoriser le travail collaboratif et une compréhension commune entre tous les membres du projets, il est important de définir, dès le début du projet, un **vocabulaire commun** autour des termes métier. Dans le jargon du développement de logiciel, on parle de [**ubiquitous language**](http://referentiel.institut-agile.fr/ubiquitous.html) ou **langage omniprésent**. C'est un principe issu de l'approche *Domain Driven Design* décrite dans l'[ouvrage](https://github.com/p0w34007/ebooks/blob/master/Eric%20Evans%202003%20-%20Domain-Driven%20Design%20-%20Tackling%20Complexity%20in%20the%20Heart%20of%20Software.pdf) du même nom et qui consiste à identifier et à définir un langage commun autour des termes métiers ce qui peut être [utile](https://promyze.com/pourquoi-lire-red-book-domain-driven-design/) dans de nombreuses situations.


Dans le cas du projet *facerecognition*, c'est un travail qui peut vous sembler fastidieux et très certainement inutile mais qui vous sera très utile pour de nombreux autres projets, notamment quand votre projet implique des développeurs et des experts métiers. Ce projet est un projet scolaire et il n'y a donc pas d'expert métiers mais pour essayer de faire comme si, vous pouvez par exemple imaginer que votre client est la DISI de l'école qui souhaite étudier la faisabilité de la reconnaissance visuelle pour contrôler les accès dans le campus plutôt que l'utilisation de badges.

Le déroulé consiste à produire ce que l'on appelle des [**User Stories**](https://en.wikipedia.org/wiki/User_story) (avec l'ensemble des parties prenantes du projet) qui représentent les besoins des utilisateurs à implémenter. Ce travail permet aussi de définir le langage partagé.

Une **user story** ce n'est rien d'autre qu'une phrase simple, en language naturel, qui permet de décrire le contenu d'une fonctionnalité à développer en précisant le *Qui?*, le *Quoi?* et le *Pourquoi?*

 `En tant que <qui>, je veux <quoi> afin de <pourquoi>`

Ici, typiquement : 

+ En tant que DISI, je veux pouvoir **constituer une base d'images annotées** des visages de l'ensemble des personnels et étudiants de l'école, à partir d'un **annuaire**, pour pouvoir mettre en place un **système de reconnaissance visuelle**.
+ En tant que DISI, je veux pouvoir **ajouter facilement une personne** au système.
+ En tant que DISI, je veux pouvoir avoir une **grande fiabilité** dans le système de reconnaissance. 
+ En tant que DISI, je veux pouvoir avoir une **alerte** si une personne n'est pas reconnue par mon système de reconnaissance faciale.
+ En tant que DISI, je veux pouvoir avoir une **reconnaissance rapide**.
+ ... 


Ici, les termes et expressions **base de données annotées**, **annuaire**, **base d'apprentissage**, **fiabilité** par exemple font partie du **langage partagé** de notre contexte. Ils pourront être utilisés indifféremment par l’ensemble des acteurs projets et désigneront toujours les mêmes concepts.

La finalité ici est de simplifier les échanges entre les différents acteurs.

Ils doivent aussi vous permettre de bien nommer les différents objets, variables, fonctions de votre application.

## Les principaux objets, modules de votre application

Cette phase d'analyse doit aussi vous faire réflechir à la conception de votre application et notamment aux différents objets et modules de cette dernière en essayant de séparer les responsabilités. 

Pour cela, essayez de réflechir à l'architecture fonctionnelle de votre application et à comment les différents acteurs, modules, objets intéragissent entre eux. Faites le avec un papier et un crayon, de manière schématique. Un travail et une reflexion de groupe peut être intéressante ici !

Prenez un peu de temps pour faire ce travail. Une fois terminé, prenez une photo de ce que vous avez mis sur papier et stockez cela dans un répertoire intitulé `WorkingDocs`de votre dépôt git. N'oubliez pas de faire un `commit` et de mettre à jour votre dépôt distant.


#### :white_check_mark: <span style="color: #26B260">A ce stade du projet, vous avez atteint le JALON 2 : Analyse et Conception de mon produit </span> 
 
L'objectif de ce travail est de vous permettre de modéliser, du point de vue informatique, votre problème mais il est essentiel aussi pour l'organisation de votre travail, c'est-à-dire, son découpage en différents sprints et fonctionnalités par exemple. 

Ici, ce travail a été fait pour vous mais, il faudra le faire pour votre projet de la semaine 2.



Nous allons maintenant passer à l'étape de développement par la réalisation de la [**Fonctionnalité 1** : Charger et afficher une image.](./Facerecognition_S1_displayimage.md)
