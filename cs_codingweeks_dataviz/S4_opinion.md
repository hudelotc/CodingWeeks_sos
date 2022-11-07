# Fonctionnalité 9 : Analyse de l'opinion


A l'aide de `Textblob`, l'objectif est d'écrire le code nécessaire à l'analyse de l'opinion pour l'évènement dans sa globalité ou pour une candidate donnée. Votre code devrait vous permettre de pouvoir mettre en oeuvre ce type d'instructions :

```PYTHON

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))
```

Pour cela, il faudra bien vous documenter sur la bibliothèque TextBlob. Quelques documentations :

 +  Documentation de référence [ici](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis).
 + [Exemple](https://medium.com/@rahulvaish/textblob-and-sentiment-analysis-python-a687e9fabe96)


Il pourra être intéressant de comparer cette analyse avec les annotations qui sont présentes dans le corpus pour évaluer la précision de l'approche d'analyse.

**Pensez à tester et à documenter votre code !!!**

ET :

+ <span style='color:blue'>le nécessaire pour le partage de votre code </span> 



Maintenant que nous avons de nouveaux outils d'analyse, nous pouvons passer à la  [**Fonctionnalité 10** : Afficher le résultat de l'analyse.](./S5_displayresult.md)