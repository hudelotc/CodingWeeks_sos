# Un système de reconnaissance faciale


L'**objectif** de ce mini-projet est de développer, de manière très incrémentale, une application autour d'une IA capable de reconnaître des personnes. L'objectif est de vous former aux bonnes pratiques de la programmation et à la culture de la qualité logicielle. Vous découvrirez lors de ce projet un ensemble d'outils pour faire de la vision par ordinateur et de l'apprentissage profond, mais vous decouvrirez surtout plusieurs principes du mouvement dit du [*Software Craftmanship*](https://www.octo.com/fr/publications/20-culture-code). 

Ce projet est très largement inspiré des tutoriaux de [Adrian Rosebrock](https://www.pyimagesearch.com/about/) en vision par ordinateur.

## A propos de la reconnaissance faciale

La [reconnaissance faciale](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_reconnaissance_faciale) est une tâche de reconnaissance visuelle qui consiste à identifier une personne à partir d'une image ou d'une vidéo de son visage. C'est une tâche qui a très longuement animé la communauté de la vision par ordinateur et pour laquelle nous avons aujourd'hui des méthodes très efficaces basées sur des techniques d'apprentissage profond et d'apprentissage par transfert. Vous pouvez lire rapidement ce [tutorial](https://towardsdatascience.com/face-recognition-for-beginners-a7a9bd5eb5c2) pour comprendre, dans les grandes lignes,  comment cela marche ou [celui là](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78) qui est très bien aussi.



L'objectif de ce projet n'est pas de vous enseigner la vision par ordinateur et l'apprentissage profond mais de vous permettre de faire un projet de programmation de bout en bout et il faudra donc accepter d'utiliser des approches sans forcement en maîtriser les principes et fondements. Nous allons notamment utiliser plusieurs bibliothèques :

+ La bibliothèque [opencv](https://pypi.org/project/opencv-python/) pour la vision par ordinateur.
+ Les bibliothèques [dlib](https://pypi.org/project/dlib/) et [keras](https://keras.io/) pour l'apprentissage profond.




## Organisation du mini-projet

Ce mini-projet est découpé en plusieurs objectifs, eux-même découpés en  **sprints** et **fonctionnalités**. La notion de sprint fait référence à la [méthode agile](https://fr.wikipedia.org/wiki/M%C3%A9thode_agile). Un sprint correspond à un intervalle de temps pendant lequel l’équipe projet va compléter un certain nombre de tâches.

Ce travail de découpage a été fait pour vous mais c'est une des premières étapes à faire pour tout projet de développement logiciel, au moins de manière macroscopique. **Pensez-y la semaine prochaine !**




### **Objectif 1 (MVP): Un système simple de reconnaissance de visage** 

Le premier objectif est de construire et d'implémenter une chaine algorithmique simple à l'aide de modules existants pour faire de la reconnaissance de visages (l'objectif principal de notre projet). Ce système pourrait être qualifié de **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)** et il pourra permettre d'avoir des premiers retours utilisateurs par exemple.

Ce concept de MVP a été popularisé par Eric Ries, l'auteur de [The Lean Startup](http://theleanstartup.com/), une approche spécifique du démarrage d'une activité économique et du lancement d'un produit. La figure ci-dessous permet de bien expliquer ce concept.

<img src="./Images/mvp.png" alt="drawing" width="500"/>

 + **Sprint 0** :
	 + [Installation du socle technique.](./Sprint0Installbis.md)
	 + [Analyse des besoins.](./Sprint0Analyse.md) 
	 + [Réflexion autour de la conception.](./Sprint0Conception.md)

+ **Sprint 1 : Prise en main d'OpenCV**
 	+ [**Fonctionnalité 1** : Charger et afficher une image.](./Facerecognition_S1_displayimage.md)
 	+ [**Fonctionnalité 2** : Effectuer un traitement sur une image et afficher le résultat du traitement.](./Facerecognition_S1_traitement.md)
 	+ [**Fonctionnalité 3** : Création d'un module d'utilitaires de manipulation d'images pour la reconnaissance de visages.](./Facerecognition_S1_moduleutils.md)


+ **Sprint 2 : Constitution d'une base de données de visages**
   + [**Fonctionnalité 4** : Structuration de la base de données](./Facerecognition_S2_database.md) 
   + [**Fonctionnalité 5** : Collecte des données](./Facerecognition_S2_databasecollect.md) 

 + **Sprint 3** : **Un module de reconnaissance visuelle par apprentissage profond**
 	+ [**Fonctionnalité 6** : Détecter un visage](./S3_facedetection.md)
 	+ [**Fonctionnalité 7** : Description des données par apprentissage profond](./S3_facedescription.md)
 	+ [**Fonctionnalité 8** : Mise en place de la reconnaissance](./S3_recognition.md)
 	+ [**Fonctionnalité 9** : Tester la reconnaissance sur la base de données](./S3_testrecognition.md)

 + **Sprint 4** : **Finalisation du MVP**
 	+ [**Fonctionnalité 10** : Un programme principal](./S4_main.md)
 	+ [**Fonctionnalité 11** : Une interface en ligne de commande avec `argparse`.](./S4_argparse.md)



### **Objectif 2 : Une application web de type Photobooth (ATTENTION, objectif difficile - A ne faire que si tout le reste est très bien fait)**

La réalisation de l'objectif 1 est une très belle étape ! Suite aux tests de votre MVP par des utilisateurs, votre client vous demande de packager cela sous la forme d'une application web de type [Photobooth](https://webcamtoy.com/).

Comme nous vous l'avons appris lors de la réalisation du premier objectif, la bonne démarche ici est donc de commencer par une phase d'analyse des besoins et de conception puis ensuite de découper l'objectif 2 en Sprints et fonctionnalités. C'est à vous de le faire cette fois-ci.

Pour vous permettre cependant de ne pas perdre trop de temps sur le partie web de l'objectif, nous vous proposons ici un tutorial sur flask qui a pour objectif de vous faire créer la page web résumant votre travail de conception. C'est [ici](flask.md).

 	





