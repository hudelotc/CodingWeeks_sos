# Fonctionnalité 8 : Prise en main de Textblob


[Textblob](https://textblob.readthedocs.io/en/dev/quickstart.html) est une bibliothèque python qui permet de faire de l'analyse de textes et de l'analyse de sentiments très rapidement. Un alternative est la bibliothèque [spacy](https://spacy.io/) qui a aussi de nombreuses fonctionnalités intéressantes. Ce sont deux bibliothéques qui reposent sur des outils d'apprentissage automatique et de traitement du langage naturel modernes (modèles de langues, représentations distribuées, apprentissage profond).


Pour commencer, il faut l'installer et la rattacher à votre projet avec par example la commande.

`pip3 install textblob` ou `pip install textblob`

## Montée en compétences sur `textblob`

Regardez et faites [le tutoriel officiel](https://textblob.readthedocs.io/en/dev/quickstart.html) pour en comprendre les fonctions principales.

Pour vous entrainer avec cette bibliothèque, écrivez une fonction `tweet_to_words` qui permet d'extraire le vocabulaire d'un ensemble de tweets en récupérant les [mots](https://textblob.readthedocs.io/en/dev/quickstart.html#tokenization), uniques et [lemmatisés](https://textblob.readthedocs.io/en/dev/quickstart.html#words-inflection-and-lemmatization). On pourra aussi supprimer de la liste obtenue les mots fréquents ou `stop-words, par exemple à l'aide de la liste fournie [ici](http://members.unine.ch/jacques.savoy/clef/frenchST.txt).

A partir de cette fonction, écrivez une fonction `corpus_frequent_words` qui affiche l'histogramme des 40 mots les plus fréquents dans votre corpus.


Il est possible que vous ne trouviez pas les résultats très bons. C'est notamment car `textblob`a été conçu pour la langue anglaise alors que notre corpus est en français.

Vous pouvez améliorer cela en utilisant l'extention [`textblob-fr`](https://github.com/sloria/textblob-fr) que vous pouvez installer avec la commande :

`pip install -U textblob-fr`
 



**Pensez à tester et à documenter votre code !!!**

Cette étape terminera votre fonctionnalité. 

Il faudra donc :

+ <span style='color:blue'>Faire le nécéssaire.</span> 

Nous pouvons maintenant passer à la [**fonctionnalité 9** : Analyse de l'opinion](./S4_opinion.md)
