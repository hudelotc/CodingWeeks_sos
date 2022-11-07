# Prise en main de tweepy et de twython - Se connecter à l'API Twitter


Pour pouvoir faire ce projet, il est nécéssaire de se connecter à Twitter et de collecter un ensemble de tweets relatifs à une entité (ou au mieux un ensemble de tweets représentatifs). 

Pour se faire, Twitter a mis à la disposition de tous un ensemble d'[API](https://fr.wikipedia.org/wiki/Interface_de_programmation)s permettant un accès programmatique à ses données. Vous avez vu le concept d'APis dans le cours de SIP mais si quelques révisions sont nécessaires, vous pouvez consultez le cours d'OpenClassRooms sur les [APIs REST](https://openclassrooms.com/fr/courses/3449001-utilisez-des-api-rest-dans-vos-projets-web). La [vidéo](https://www.lewagon.com/fr/blog/api-webhook-debutant-tutoriel) du tutorial de S. Saunier du Wagon est aussi une très bonne introduction pour les débutants.

Les APIs Twitter sont nombreuses et très bien décrites [ici](https://developer.twitter.com/en/docs.html). Celle qui nous intéresse particulièrement ici est l'API [**Search**](https://developer.twitter.com/en/docs/tweets/search/overview) qui permet de récupérer des tweets historiques à partir de mots clés. Twitter a recemment revu sa politique de mise à disposition de ses données et de facturation de cette dernière et la recherche se limite maintenant à 7 jours précédents la recherche.

De nombreux outils ont été développés pour faciliter l'utilisation de ces APIs et notamment en python, plusieurs biblithèques sont disponibles :

+ [tweepy](http://www.tweepy.org/)
+ [python_tweeter](https://github.com/bear/python-twitter)
+ [twython](https://github.com/ryanmcgrath/twython )
+ ...

Dans ce projet, nous allons utiliser twython (pour récupérer les données du corpus) et Tweepy (pour apliquer le modèle d'opinions à de nouvelles données) qui sont des bibliothèques qui permettent d'accéder relativement facilement aux APIS twitter. La première chose à faire est donc d'installer tweepy ou twython via la commande:

`pip install tweepy`
`pip install twython`


Vous pouvez tester l'installation en exécutant l'instruction `import tweepy` ou `import twython` sur votre interpréteur python. 

## Etape 1 : se créer un compte twitter.

La première étape pour cette fonctionnalité est de se créer un compte Twitter si vous n'en avez pas car il est nécessaire pour pouvoir avoir accès à l'API.


Après avoir créé votre compte, il est nécessaire d'aller sur le [portail de gestion des applications](https://developer.twitter.com/en/apps) pour demander une compte `developper` et créer une `app` ce qui peut être une procédure assez longue.
Pour faciliter l'utilisation de l'API twitter dans le contexte académique, la procédure est facilitée en créant un groupe académique. Pour cela, il faudra faire une liste des identifiants Twitter des différentes personnes d'un groupe pour vous ajouter dans ce groupe.


L'autre possibilité est de démander la création d'un compte developper personnel. On rentre ici dans un processus assez long (un questionnaire avec pas mal de champ à compléter) qui passe par le dépôt d'une demande de candidature pour avoir un compte `developper` et avoir accès au [portail developper](developer.twitter.com.). Pour cela, il faudra faire attention a remplir les champs correctement pour que la validation de votre compte developpeur soit valide.

Exemple montrant comment compléter cela :

```
### Information for the twitter developper account
# Twitter account


### How will you use the Twitter API or Twitter data?


#### In your words

Use of twitter API as part of a programming contest course in CentraleSupelec engineering School in France. The aim of the course is to built from scratch an app that will collect tweets related to an event, analyze them using the python data science librairies and visualize the result of the analysis.  The instructor is Celine Hudelot, course named Coding Weeks. The details of this course can be found here : https://gitlab-ovh-03.cloud.centralesupelec.fr/celine.hudelot/cs_codingweek_dataviz_2021.



####The specifics

#### Are you planning to analyze Twitter data? ==== > YES

The content of the tweet will be used in order to perform task such as opinion mining, sentiment analysis or to compute some general statistics on the tweets and their words.


#### Will your app use Tweet, Retweet, like, follow, or Direct Message functionality?==== > YES

Yes. We will use them just to have some information of popularity on a tweet or an event and to complete the opinion mining analysis.


#### Do you plan to display Tweets or aggregate data about Twitter content outside of Twitter?
 
 Yes, but not the full content of the tweets. We will build a visualization app that enable the visualization of the result of the analysis such as histrograms, barcharts. All the work will be done on internal servers in our school and will not be exposed outside of the institution.

#### Will your product, service or analysis make Twitter content or derived information available to a government entity? ==== > NO
```


Une fois là, vous pouvez maintenant créer une `app` en complétant encore une fois l'ensemble des informations demandées.

**Exemple**

**App Name**

cs_week_twitter_2021

**Description**

AcademicProject in the context of a programming course

**Website URL**

https://gitlab-ovh-03.cloud.centralesupelec.fr/celine.hudelot/cs_codingweek_dataviz_2021

**Sign in with Twitter**

Disabled

**Organization name**

CentraleSupélec

**Organization website URL**


https://www.centralesupelec.fr/

**App usage**

This app will juste be used to collect some tweet related to a specific event in order to build an application of opinion mining. This is in the context of an academic activity that aims at giving students some skills in programming and data science such as :

 + using versonning
 + building an application from scratch
 + using apis
 + using the data science python framework



**<span style='color:red'> Cette étape peut être un peu longue et en attendant d'avoir accès aux API de Twitter, vous pouvez revenir à [**Fonctionnalité 1** : Prise en main du corpus Canephore.](./S1_corpuspriseenmain.md)




Après cette étape, vous pouvez maintenant récupérer vos `Consumer API keys` et `Access token & access token secret` nécéssaires pour se connecter.

Vous sauverez les différentes valeurs de :

+ Consumer Key (API Key)
+ Consumer Secret (API Secret)
+ Access Token
+ Access Token Secret

dans un fichier `credentials.py` dont le squelette pourrait être le suivant :

```PYTHON
# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = ''
CONSUMER_SECRET = ''

# Access:
ACCESS_TOKEN  = ''
ACCESS_SECRET = ''

```

**<span style='color:red'> Attention, ce fichier ne sera jamais mis sur votre dépôt git (ni local, et surtout pas distant)</span>**


## Etape 2 : le Hello Word de Tweepy

Vous pouvez maintenant faire le *Hello World* de Tweepy qui consiste en une fonction d'initialisation de l'API Twitter.

```PYTHON
import tweepy
# We import our access keys:
from tweet_collection.credentials import *   

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

```

Sur cette base, nous allons maintenant initialiser notre module de collecte de tweets. Ajouter à votre projet un package nommé `twitter_collect` (création d'un fichier `__init__.py` dans le répertoire correspondant à votre package).

Au passage, voici un petit rappel sur les [modules et les packages](https://docs.python.org/fr/3/tutorial/modules.html) en python.


Dans le package `twitter_collect`, ajouter un module `twitter_connection_setup` (un fichier `twitter_connection_setup.py`) dans lequel vous écrirez donc les fonctions nécessaires pour une connexion à l'API Twitter.




A l'aide de `pytest`, **tester**  votre fonction de connexion à l'API ! Nous verrons plus tard une méthode de developpement appelée **Test Driven Development** qui consiste à écrire les tests avant les fonctions ou autres objets de votre programme mais en attendant, prenez le temps d'ajouter les tests permettant de tester les différentes fonctionnalités de votre projet. 

Ici par exemple, il s'agit d'ajouter un module `test_monmodule.py` à votre projet et de tester que la fonction de connexion à l'API vous renvoit bien un objet non nul.


Nous avons fini ici la fonctionnalité 1. Avant de passer à la fonctionnalité suivante, il vous est demandé de :


+ <span style='color:blue'>Ajouter votre fichier à votre dépôt git.</span>
+ <span style='color:blue'>Faire un commit</span>
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 



## Un peu de prise de recul

Vous avez peut-être trouvé cette première étape assez pénible et avec de nombreuses étapes de création de comptes et d'engagement, beaucoup de formulaires assez détaillés à remplir ... Pour éviter ces étapes, une alternative aurait été de vous founir un jeu de données et de vous faire travailler directement sur ce jeu de données mais il est important de connaître des contraintes et de savoir utiliser des APis.


Plus globalement, que sommes-nous en train de faire ? Certaines [actualités récentes](https://www.lemonde.fr/pixels/video/2018/04/14/comment-facebook-peut-il-influencer-le-resultat-d-une-election_5285587_4408996.html), les [scandales](https://www.sciencesetavenir.fr/high-tech/election-de-trump-facebook-bloque-cambridge-analytica_122162) autour de la société Cambridge Analytica, le [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es)... devraient vous permettre de comprendre pourquoi l'accès à ce type de données devient de plus en plus controlé.

Prenez donc le temps de lire rapidement les [règles et les politiques](https://help.twitter.com/fr/rules-and-policies/twitter-api) d'accès aux données de Twitter.

Une fois cela fait, vous pouvez maintenant vous intéresser à la mise en place d'un outil de collecte de tweets en français.


Maintenant que nous avons établi une connexion avec l'API Twitter, nous allons utiliser cette connexion pour collecter des tweets. En particulier, avec les APIs de Twitter nous pouvons :

+ recupérer des tweets historiques (de 7 jours précédents) à l'aide de mots clés (`API Search`)
+ récupérer les tweets et l'activité d'un utilisateur donné (`API Users`)
+ capter et filtrer un flux de tweets en temps réel (`API Streaming and Filter`)


Attention, l'accès à ces différentes APIs est limité. Les règles sont [ici](https://developer.twitter.com/en/docs/basics/rate-limiting.html). 


## Etape 1 : Prise en main de l'API [Search](https://developer.twitter.com/en/docs/tweets/search/overview)

Nous allons ici prendre en main l'API `Search` à l'aide de Tweepy. Rappelez-vous que l'utilisation aux APIs de Twitter est limitée et prenez donc le temps de bien reflechir à ce que vous faites.


La documentation générale de ce que permet Tweepy est disponible [ici](http://docs.tweepy.org/en/v3.6.0/api.html).

Voici en particulier la documentation de la fonction `search`.

```
API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])
```

qui renvoie les tweets qui sont en correspondance avec la requête `q`

avec les paramètres suivants:	

+ `q` – the search query string
+ `lang` – Restricts tweets to the given language, given by an ISO 639-1 code.
+ `locale` – Specify the language of the query you are sending. This is intended for language-specific clients and the default should work in the majority of cases.
+ `rpp` – The number of tweets to return per page, up to a max of 100.
+ `page` – The page number (starting at 1) to return, up to a max of roughly 1500 results (based on rpp * page.
+ `since_id` – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
+ `geocode` – Returns tweets by users located + `show_user` – When true, prepends “<user>:” to the beginning of the tweet. This is useful for readers that do not display Atom’s author field. The default is false.


+ Ecrire un outil de collecte avec l'`API Search` .
+ Lancer une analyse d'opinions sur les tweets collectés.
+ Visualiser les résultats de l'analyse.

Et bien-sûr, <span style='color:blue'> Finaliser tout cela très proprement </span> 






