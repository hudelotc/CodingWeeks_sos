# Simulation physique : le pendule et autres cas illustratifs

L'**objectif** de ce mini-projet est de développer, de manière très incrémentale, la simulation d'un pendule et d'éventuels autres systèmes physiques et l'animation de cette simulation afin de vous former aux bonnes pratiques de la programmation et à la culture de la qualité logicielle. En particulier, au travers de ce projet, vous allez découvrir plusieurs principes du mouvement dit du [*Software Craftmanship*](https://www.octo.com/fr/publications/20-culture-code). 





## A propos de la modélisation numérique et de la simulation physique 

La modélisation numérique est la transcription d'un phénomène physique en langage informatique. Elle consiste à transformer une réalité physique en des modèles abstraits, aussi proches que possibles de la réalité du système, accessibles à l'analyse et au calcul.  

La simulation numérique est le processus qui permet de calculer, sur
ordinateur, les solutions de ces modèles et donc de simuler la réalité physique. Elle permet donc de faire des expériences virtuelles sur le comportement du modèle.

L'objectif de ce projet n'est pas de vous enseigner la modélisation et la simulation numérique mais de vous faire acquérir des compétences en programmation et en développement logiciel à l'aide d'un projet de programmation de bout en bout et il faudra donc accepter d'utiliser des approches sans forcement les maîtriser intégralement. L'objectif aussi est de vous familiariser avec quelques-unes des bibliothèques python qui sont très utiles dans ce contexte :


+ La bibliothèque [scipy](https://www.scipy.org/) qui est un ensemble d’outils logiciels facilitant la programmation scientifique et qui inclut plusieurs paquets dont :
	+ [Numpy](https://numpy.org/), pour le calcul numérique;
	+ [Matplotlib](https://matplotlib.org/), pour créer des dessins et des animations;
	+ [Sympy](https://www.sympy.org/en/index.html), pour le calcul symbolique;
	+ ...
+ la bibliothèque [pymunk](http://www.pymunk.org/en/latest/), un moteur de physique 2d, facile à utiliser, construit au dessus de la bibliothèque de physique 2d [Chipmunk](https://chipmunk-physics.net/).
+ et d'autres comme [PyODE](http://pyode.sourceforge.net/) par exemple.
	
En terme de finalité de notre application, un bon exemple d'objectif est par exemple [ce type d'application](https://www.myphysicslab.com/pendulum/pendulum-en.html) :

<img src="./Images/applipendule.png" alt="drawing" width="600"/>


## Le problème du pendule

En physique, le pendule simple est une masse ponctuelle fixée à l'extrémité d'un fil sans masse, inextensible et sans raideur et qui oscille sous l'effet de la pesanteur. Il s'agit du modèle de pendule pesant le plus simple. 

On considère donc comme état du système, les conditions suivantes :

+ Une extrémité est fixée;
+ L’autre extrémité est libre;
+ On suppose que la ficelle est toujours pleinement tendue;
+ On suppose qu’il n’y a aucune friction.
+ Pour modéliser le problème, il faudrait connaître  <a href="https://www.codecogs.com/eqnedit.php?latex=\theta(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta(t)" title="\theta(t)" /></a>, l'angle du pendule à l'instant t.


### Equation de mouvement du pendule

L'objectif n'étant pas d'enseigner la modélisation, on rappelle ici l'équation de mouvement du pendule.

<img src="./Images/Pendulum.gif" alt="drawing" width="150"/>


Un pendule simple est une masse <i>m</i> fixée à l'extrémité *P* d'un fil de longeur *L*. Quand on le déplace d'un angle fixé et qu'on le relâche, le pendule va osciller de manière périodique.   En appliquant la seconde loi de Newton, on obtient l'équation de mouvement du pendule ci-dessous


<img src="./Images/CodeCogsEqn.gif" alt="drawing" width="300"/>



En effet :

 + le vecteur vitesse de la boule est toujours perpendiculaire à la ficelle;
 + Par conséquent, la composante de la force de gravité agissant de façon perpendiculaire à la ficelle est donnée par

<a href="https://www.codecogs.com/eqnedit.php?latex=F&space;=&space;-mg&space;\sin\theta&space;=&space;ma&space;\Rightarrow&space;a&space;=&space;-g&space;\sin\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F&space;=&space;-mg&space;\sin\theta&space;=&space;ma&space;\Rightarrow&space;a&space;=&space;-g&space;\sin\theta" title="F = -mg \sin\theta = ma \Rightarrow a = -g \sin\theta" /></a>

 + L'accélération angulaire est donnée par 

<a href="https://www.codecogs.com/eqnedit.php?latex=a&space;=&space;L&space;\frac{d^2\theta}{dt^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a&space;=&space;L&space;\frac{d^2\theta}{dt^2}" title="a = L \frac{d^2\theta}{dt^2}" /></a>


On obtient bien en combinant l'équation définie ci-dessus que l'on peut transformer en :

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d^2\theta}{dt^2}&space;&plus;&space;\frac{g}{L}\sin\theta&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{d^2\theta}{dt^2}&space;&plus;&space;\frac{g}{L}\sin\theta&space;=&space;0" title="\frac{d^2\theta}{dt^2} + \frac{g}{L}\sin\theta = 0" /></a>

Cette équation est difficile à résoudre de manière exacte mais par contre si l'amplitude du déplacement angulaire est petite, on a alors l'approximation <a href="https://www.codecogs.com/eqnedit.php?latex=\sin\theta\approx\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sin\theta\approx\theta" title="\sin\theta\approx\theta" /></a> ce qui permet d'obtenir alors une équation du premier ordre linéaire.

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d^2\theta}{dt^2}&space;&plus;&space;\frac{g}{L}\theta&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{d^2\theta}{dt^2}&space;&plus;&space;\frac{g}{L}\theta&space;=&space;0" title="\frac{d^2\theta}{dt^2} + \frac{g}{L}\theta = 0" /></a>

Une solution harmonique simple est
<a href="https://www.codecogs.com/eqnedit.php?latex=\theta(t)&space;=&space;\theta_o&space;\cos(\omega&space;t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta(t)&space;=&space;\theta_o&space;\cos(\omega&space;t)" title="\theta(t) = \theta_o \cos(\omega t)" /></a> 
avec <a href="https://www.codecogs.com/eqnedit.php?latex=\theta_o" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta_o" title="\theta_o" /></a> le déplacement angulaire initial, et <a href="https://www.codecogs.com/eqnedit.php?latex=\omega&space;=&space;\sqrt{g/L}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\omega&space;=&space;\sqrt{g/L}" title="\omega = \sqrt{g/L}" /></a>  la fréquence du mouvement.  La période est :


<a href="https://www.codecogs.com/eqnedit.php?latex=T&space;=&space;\frac{2\pi}{\omega}&space;=&space;2\pi\sqrt{\frac{L}{g}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T&space;=&space;\frac{2\pi}{\omega}&space;=&space;2\pi\sqrt{\frac{L}{g}}" title="T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{L}{g}}" /></a>


Quand l’approximation <a href="https://www.codecogs.com/eqnedit.php?latex=\sin\theta\approx\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sin\theta\approx\theta" title="\sin\theta\approx\theta" /></a> n’est pas valide, il faut intégrer numériquement l'équation différentielle pour obtenir l’évolution de la position et de la vitesse angulaire du pendule, au cours du temps.

Il faut alors disposer d’un intégrateur d’équations différentielles que nous trouverons dans `scipy`.


 Nous allons maintenant nous intéresser à la simulation du pendule et à sa visualisation.

## Organisation du mini-projet

Ce mini-projet est découpé en plusieurs objectifs, eux-même découpés en  **sprints** et **fonctionnalités**. La notion de sprint fait référence à la [méthode agile](https://fr.wikipedia.org/wiki/M%C3%A9thode_agile). Un sprint correspond à un intervalle de temps pendant lequel l’équipe projet va compléter un certain nombre de tâches.

Ce travail de découpage a été fait pour vous pour le début de ce projet mais c'est une des premières étapes à faire pour tout projet de développement logiciel, au moins de manière macroscopique. **Pensez-y la semaine prochaine !**

### **Objectif 1 (MVP): Un pendule simple avec `matplotlib`** 

Le premier objectif de cette semaine est de constuire et d'implémenter la simulation et la visualisation du mouvement d'un pendule simple avec `matplotlib` et c'est ce qui constituera notre **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)**. 

Ce concept de MVP a été popularisé par Eric Ries, l'auteur de [The Lean Startup](http://theleanstartup.com/), une approche spécifique de démarrage d'une activité économique et de lancement d'un produit. La figure ci-dessous permet de bien expliquer ce concept.


![MVP](./Images/mvp.png)

 + **Sprint 0** :
	 + [Installation du socle technique.](./Sprint0Installbis.md)
	 + [Analyse des besoins.](./Sprint0Analyse.md) 
	 + [Refexion autour de la conception.](./Sprint0Conception.md)

 + **Sprint 1 : Mise en place du modèle du pendule**
 	+ [**Fonctionnalité 1** : représentation d'un pendule.](./pendulum_S1_pendule.md)
 	+ [**Fonctionnalité 2** : affichage du pendule](pendule_S1_visualisation.md)
 	 		
 + **Sprint 2** : **Mise en mouvement du pendule**
 	+ [**Fonctionnalité 3** : simulation du mouvement d'un pendule](./S2_pendule_motion.md) 
 	+ [**Fonctionnalité 4** : Une première animation avec matplotlib
](./S2_simpleanimation.md)
 	+ [**Fonctionnalité 5** : visualisation du mouvement et de la vitesse du pendule au cours du temps](./S2_motionvisualisation.md)

 + **Sprint 3** : **Paramétrer et lancer la simulation en ligne de commande**
 	+ 	[**Fonctionnalité 6** : Prise en main du module `argparse`](./S3_argparse.md) 
 	+  [**Fonctionnalité 7** : Un programme principal](./S4_gamemain.md) 
 	+  [**Fonctionnalité 8** : Un pendule en ligne de commande](./S3_pendulum_mvp.md) 


 	
### **Objectif 2: Un pendule avec une interface graphique** 

+ **Sprint 4** : **Montée en compétences : les interfaces graphiques en python**

 	+ [**Fonctionnalité 9** : Premiers pas en Tkinter](S4_GUI_Tutorial.md)

 + 	**Sprint 5** : **Une interface graphique pour le pendule**
 	
 	+ [**Fonctionnalité 10** : Une interface graphique pour le pendule : maquette](S4_GUI_pendulum_mock.md)
 	+ [**Fonctionnalité 11** : Une interface graphique pour le pendule](S4_GUI_pendulum.md)
 	+ [**Fonctionnalité 12** : Permettre la configuration du pendule via l'interface graphique](config.md)

 	
### **Objectif 3 : un pendule avec `pymunk`** 	
[`pymunk`](http://www.pymunk.org/en/latest/) est un moteur de physique 2d, facile à utiliser, construit au dessus de la bibliothèque de physique 2d [Chipmunk](https://chipmunk-physics.net/). Elle est très facile à utiliser et pensez-y à chaque fois que vous avez besoin de la physique 2d des corps rigides en Python.


La première chose à faire est d'installer cette bibliothèque avec la commande :

`pip install pymunk` ou `pip3 install pymunk` 

Si vous passez par anaconda, la commande ci-dessous permettra aussi de l'installer.

Pour réaliser cet objectif, il faudra d'abord vous familiariser avec `pymunk`, par exemple en suivant son tutorial [ici](http://www.pymunk.org/en/latest/tutorials/SlideAndPinJoint.html).

Après avoir suivi, ce tutorial, une étape intéressante peut-être de regarder si `pymunk` propose déjà un exemple de simulation de pendule. C'est le cas [ici](https://pymunk-tutorial.readthedocs.io/en/latest/intro/intro.html#pin-joint).


Vous êtes prêts maintenant à écrire votre propre version de simulation du pendule avec `pymunk` . A vous de jouer ! Il faudra bien sûr pour cela appliquer les mêmes méthodologies que pour l'objectif 1 et l'objectif 2. Avant de vous lancer, il faudra donc découper votre travail en sprints. Un document décrivant votre découpage devra d'ailleurs être déposé sur l'espace Gitlab de votre projet. 


### **Objectif 4 : Améliorations, autre modélisation et simulation.**

A ce stage du projet, les objectifs sont complétement atteints et il convient alors de refaire un cycle de conception après avoir eu des retours utilisateurs.
Plusieurs fonctionnalités pourraient être ajoutées à votre projet ou vous pourriez vouloir l'étendre en ajoutant par exemple d'autres fonctionnalités.

C'est à vous de décider. Ici aussi votre travail se fera en appliquant les mêmes méthodologies que pour l'objectif 1 et l'objectif 2. Avant de vous lancer, il faudra donc découper votre travail en sprints. Un document décrivant votre découpage devra d'ailleurs être déposé sur l'espace Gitlab de votre projet.








