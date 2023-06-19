# Simulation physique - Sprint 0 : Analyse du problème

Une des premières étapes de tout travail de programmation et de développement logiciel, quelque soit la méthodologie de développement utilisée, consiste à réaliser une rapide **analyse des besoins**, avant toute phase d'implémentation.

Cette analyse a pour objectif d'identifier les principales fonctionnalités à développer pour avoir le comportement souhaité du système développé. Cette première liste de fonctionnalités n'a pas besoin d'être exhaustive, ni figée, mais elle vous permettra de construire vos premiers développements.


## Analyse des besoins : les principales fonctionnalités

L'objectif ici est de permettre à un utilisateur de pouvoir étudier le comportement d'un système physique au travers de la simulation numérique et de la visualisation. Il s'agira donc de concevoir un logiciel permettant à un utilisateur d'intéragir avec une ou plusieurs simulations physiques, d'abord en mode console, sans interface graphique.



Le **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)** de ce projet consistera à livrer une première simulation d'un phénomène physique, dans notre cas le pendule, avec une intéraction en mode console. Votre solution

+  **Permettra à un utilisateur de choisir les différents paramètres de la simulation du pendule : la vitesse initiale, la longeur de la tige...**
+  **Permettra la simulation et la visualisation de cette dernière en fonction des paramètres rentrés par l'utilisateur**.
+  **Affichera la simulation sous la forme d'une animation à l'aide du module animation de `matplotlib`**
+  **Permettra de mettre en avant les différents paramètres et phénomènes connus du modèle du pendule**


D'autres fonctionnalités pourront bien sûr être ajoutées ensuite pour améliorer la simulation après avoir fini ce MVP. En permettant un prototype de simulation rapide, vous pourrez confronter rapidement votre produit à ses utilisateurs. Imaginez que vos utilisateurs sont des lycéens à qui on veut faire comprendre le phénomène physique en l'obervant par simulations. Ils pourront vous donner assez vite des retours sur les fonctionnalités manquantes pour atteindre cet objectif.


Vous pouvez maintenant continuez par le [Sprint 0 : Reflexion autour de la conception](./Sprint0Conception.md).