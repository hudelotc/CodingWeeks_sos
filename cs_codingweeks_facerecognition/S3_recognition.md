# Fonctionnalité 8: Mise en place de la reconnaissance

Pour chaque image de notre base, nous avons grâce à l'étape précédente un vecteur la décrivant. Pour la reconnaissance en tant que telle, nous allons mettre en place une approche par plus proches voisins.

Le principe est le suivant. Etant donnée une nouvelle image, cette image est passée dans le réseau VGG pour en obtenir son vecteur de représentation (après une étape de détection et de redimensionnement) puis elle est comparée avec les vecteurs de représentations de chaque image de la base. La classe (ou le nom du repertoire) de l'image la plus proche est affectée à la nouvelle image.

Ecrivez le programme permettant de mettre en oeuvre ce mécanisme. Tester le et comme d'habitude.

+ <span style='color:blue'>Faire un commit dès que la réalisation d'une fonctionnalité ou d'une sous-fonctionnalité est finie.</span> 
+ <span style='color:blue'>Tagger à la fin de chaque journée votre dernier commit </span> 
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 




Vous pouvez passer maintenant à la [**Fonctionnalité 9** : Tester la reconnaissance sur la base de données](./S3_testrecognition.md)