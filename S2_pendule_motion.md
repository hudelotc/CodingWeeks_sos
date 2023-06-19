# Fonctionnalité 3: simulation du mouvement d'un pendule

Cette fonctionnalité consiste à mettre en mouvement le pendule. Il s'agit donc ici de mettre en programme l'équation du mouvement du pendule. Pour cette fonctionnalité, on fera appel à des solveurs d'équations différentielles de la bibliothèque [scipy](https://www.scipy.org/) et en particulier ce [solveur](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp).

Le principe est très bien expliqué sur ce [tutoriel](https://python-prepa.github.io/systemes_dynamiques.html)

Créer un module `pendulum_simulation_motion.py` dans le package `pendulum` dans lequel nous allons écrire les fonctions nécessaires à cette simulation. 


## Etape 1 : Definition des paramètres initiaux de la simulation.

Dans le module `pendulum_simulation_motion.py`, écrire une fonction `initiate_simulation` qui permet d'initialiser les différentes paramètres de la simulation comme :

 + l'accélération due à la gravité et qui aura comme valeur par défaut `9.8`.
 +  l'angle et la vitesse initiale.
 +  ...


## Etape 2 : Ecriture des équations à résoudre dans une fonction


Ajouter et écrire la fonction `simple_pendulum_ODE` dans le module `pendulum_simulation_motion.py` qui, étant donné un pendule de longeur *L* et une valeur d'accélération due à la gravité,  transforme l’équation différentielle du 2nd ordre régissant le mouvement du pendule  sous la forme d’un système d’équations du premier ordre comme expliqué [ici](https://python-prepa.github.io/systemes_dynamiques.html)
)

Nous vous laissons libre de choisir comment réaliser cette fonctionnalité. Il est attendu du code commenté permettant de réaliser cette fonctionnalité et les tests associés. Vous pouvez librement appliquer la méthodologie TDD ou non.

Ici par exemple un test à passer, parmi d'autres, pourrait être

```PYTHON
from pendulum.pendulum_simulation_motion import *
from pytest import *
import numpy as np


def test_simple_pendulum_ODE():
    #Given
    gravity = 9.8
    length = 10
    Y0 = np.array([np.pi / 2.0, 0])
    t=0
    #When
    second_term = simple_pendulum_ODE(Y0,t,length,gravity)
    #Then
    assert np.allclose(second_term,np.array([ 0.,-0.98])) == True
```




## Etape 3 : recherche d'une solution par intégration d'une trajectoire à partir d’une condition initiale


Ajouter la fonction `find_solution` qui permet de trouver une solution en intégrant numériquement les équations du mouvement afin d'obtenir l’évolution de la position et de la vitesse angulaire du pendule, au cours du temps. On fera appel pour cette étape aux solveurs de la bibliothèque `scipy` et en particulier le solveur [`solve_idp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp) ou [`ode_int`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html#scipy.integrate.odeint) dont un exemple d'utilisation est disponible [ici](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html#ordinary-differential-equations-odeint). `ode_int` est très répandu mais il est obsolète dans les dernières versions de scipy et il est donc préférable d'utiliser `solve_idp`.

D'autres fonctions sont disponibles dans le module [`integrate`](https://docs.scipy.org/doc/scipy/reference/integrate.html#solving-initial-value-problems-for-ode-systems) de scipy.

Pour écrire cette fonction vous devrez aussi faire appel à la fonction `linspace` de numpy qui permet d’obtenir un tableau 1D allant d’une valeur de départ à une valeur de fin avec un nombre donné d’éléments et qui permettra de définir l'échantillonage temporel. Il faudra faire en sorte que cette fonction soit la plus générique et paramétrable possible.



**N'oubliez pas de mettre à jour votre dépôt local et distant comme nous l'avons vu dans le tutorial git.** 

Vous pouvez passer à la [**Fonctionnalité 4** : Une première animation avec matplotlib
](./S2_simpleanimation.md)





