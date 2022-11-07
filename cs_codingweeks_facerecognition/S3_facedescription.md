# Fonctionnalité 7 : Description des données - Embeddings

L'objectif ici est d'utiliser une approche d'apprentissage profond pour apprendre une représentation utile de l'image sous la forme d'un vecteur de caractéristiques. Dans le cadre de ce projet, on ne va pas entraîner de réseaux profonds mais nous allons faire ce que l'on appelle de **l'apprentissage par transfert**. 

Cela consiste à utiliser un réseau pré-entraîné et on va l'utiliser pour construire une représentation vectorielle de chacune des images de notre base.

En particulier, nous allons utiliser le modèle [VGG Face](http://www.robots.ox.ac.uk/~vgg/data/vgg_face/) entraîné sur une grosse base de données décrite [ici](http://www.robots.ox.ac.uk/~vgg/data/vgg_face2/).

Pour cela, nous allons utiliser la bibliothèque d'apprentissage profond [keras](https://keras.io/) qu'il vous faudra installer et prendre en main.

Pour cela nous vous proposons de suivre ce [mini tutoriel](intro_keras.md).

Une fois ce tutoriel fait, alors il faudra mettre en place la chaîne de description de vos données avec VGG Face.

Plusieurs options sont possibles ici :

 + L'utilisation de [`keras-vggface`](https://github.com/rcmalli/keras-vggface) qui est une bibliothèque dédiée à l'utilisation des modèles VGG Face au sein de Keras (plus facile, avec peut être des problèmes d'installations)
 + La reproduction de l'architecture du réseau VGGFace avec Keras puis le chargement des poids appris sur le jeu de données de VGG Face et mis à disposition [ici](https://github.com/ox-vgg/vgg_face2) (nécessite plus de compréhension de l'apprentissage profond et des réseaux de neurônes convolutionnels).

 
Voici quelques éléments indicatifs pour l'approche 1.

 + Installer `keras-vggface` avec la commande 

 `pip install git+https://github.com/rcmalli/keras-vggface.git `
 
 + Vérifier que la bibliothèque s'est bien installée avec `import keras_vggface`
 
 + Le modèle prend en entrée des images de taille `224 x 224` et il est donc nécessaire ici de faire appel à votre module de détection de visages pour extraire l'enveloppe du visage et ensuite la redimensionner dans la bonne taille (Vous pourrez notamment tester cette fonction en vérifiant que l'image de sortie fait bien la taille attendue).

 + Enfin, il vous faudra écrire une programme dans lequel vous créer et charger un modèle VGG. Par exemple, la commande ci-dessous permet de charger le modèle [`RESNET50`](https://arxiv.org/abs/1512.03385).

 `model = VGGFace(model='resnet50')`
 
 + Vous pouvez regarder les entrées et les sorties du modèles avec :

	```PYTHON
	print('Inputs: %s' % model.inputs)
	print('Outputs: %s' % model.outputs)
	```
Nous retrouvons bien la taille de `224 x 224` en entrée et la taille du vecteur de sortie est de 8631, ce qui correspond aux 8631 personnalités du jeu de données [MS_Celeb-1M Dataset](https://www.microsoft.com/en-us/research/project/ms-celeb-1m-challenge-recognizing-one-million-celebrities-real-world/).

 + Dans notre cas, nous aimerions récupérer les couches internes du réseau et non pas la sortie de la classification et il faudra donc charger le modèle comme cela :

 `model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')`
 
 + Il suffit après d'appeler la fonction `predict` sur l'échantillon `samples` de données que l'on souhaite prédire comme ci-dessous

 `model.predict(samples)`
 
 
 Pensez à bien regarder le peu de documentation disponible sur ce package [ici](https://github.com/rcmalli/keras-vggface).
 
 
Si vous avez compris comme tout cela marche, il vous reste à écrire une fonction qui permet de générer et de stocker les descriptions (ou embeddings) d'une image donnée ou de l'ensemble des images de la base. Il vous faudra réfléchir à la structure de données utilisée pour avoir cette information de description pour toutes les images de la base.
 
 
Petit rappel comme d'habitude.

+ <span style='color:blue'>Faire un commit dès que la réalisation d'une fonctionnalité ou d'une sous-fonctionnalité est finie.</span> 
+ <span style='color:blue'>Tagger à la fin de chaque journée votre dernier commit et tagger à la fin de chaue fonctionnalité </span> 
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 
+ <span style='color:blue'>Faire un test de couverture de code à la fin de chaque journée et de pousser le bilan obtenu vers votre dépôt distant sur GitLab.</span>

Vous pouvez passer maintenant à la [**Fonctionnalité 8** : Tester la reconnaissance sur la base de données](./S3_recognition.md)
 

 

 
 

 
 



