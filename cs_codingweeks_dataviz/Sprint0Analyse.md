# DataVisualization - Sprint 0 : Analyse du problème

Une des premières étapes de tout travail de programmation et de développement logiciel, quelque soit la méthodologie de développement utilisée, consiste à réaliser une rapide **analyse des besoins**, avant toute phase d'implémentation.

Cette analyse a pour objectif d'identifier les principales fonctionnalités à développer pour avoir le comportement souhaité du système développé. Cette première liste de fonctionnalités n'a pas besoin d'être exhaustive, ni figée, mais elle vous permettra de construire vos premiers développements.


## Analyse des besoins : les principales fonctionnalités

L'objectif ici est de pouvoir valoriser, au travers d'un dashboard de visualisation, les résultats d'une analyse. C'est un besoin très important et qui trouve de nombreuses applications : voir par exemple [cet article](https://academy.visiplus.com/blog/analytics-2/la-data-visualisation-pour-une-meilleure-experience-client-2017-06-16).

On s'intéresse ici à des données sociales, un ensemble de tweets relatifs à un évènement, l'élection Miss France 2012. Permettre une visualisation de l'opinion de la sphère sociale concernant ce type d'évènements pourrait, par exemple, servir aux organisateurs pour améliorer les prochaines éditions de l'évènement. 


Le **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)** de ce projet consistera à livrer une première version de l'outil de visualisation, c'est-à-dire un outil mettant en oeuvre la chaine classique d'analyse de données : leur récupération, leur analyse et la visualisation de cette analyse avec une ou deux [techniques de visualisations communes](https://academy.visiplus.com/blog/analytics-2/conception-de-dashboard-les-fondamentaux-de-la-data-visualisation-2017-09-06). C'est une chaine classique de **valorisation de données**.


En particulier, le MVP : 

+ **Permettra de récupérer les tweets encore existants donnés dans le corpus**.
+ **Utilisera les annotations fournies dans le corpus pour une première analyse de données très simple**.
+  **Se basera uniquement sur l'analyse du contenu textuel des tweets et négligera l'information sur l'auteur du tweet, son type (*retweet*, *reply*,...) et son contenu multimédia**.
+ **Permettra un traitement et une analyse des tweets.**
+ **Affichera les résultats de l'analyse sous la forme de visualisations communes comme par exemples des histogrammes ou des diagrammes en camenbert**.

 
D'autres fonctionnalités pourront bien sûr être ajoutées ensuite pour améliorer votre projet après avoir fini ce MVP. En construisant rapidement une chaîne de bout en bout, vous pourrez cependant rapidement avoir des retours sur votre produit et ses fonctionnalités et utiliser ces retours pour l'améliorer.

Vous pouvez maintenant continuer par le [Sprint 0 : Reflexion autour de la conception](./Sprint0Conception.md).