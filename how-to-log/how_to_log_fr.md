---
title: Comment rendre les logs utiles ?
author: Ismaël Maurice
date: 28/09/2024
---

<img src="./img/splash.jpg" alt="" width="100%" height="500px" />

[Source Image](https://unsplash.com/fr/photos/ordinateur-portable-noir-allume-f5pTwLHCsAg)

# Comment rendre les logs utiles ?

En tant que développeurs, les logs constituent la partie expressive de notre application. Ils permettent de capturer l’activité d’une application.

En programmation informatique, un développeur peut décider d’afficher ou non les logs dans son application qui peut être une aide de traçabilité en cas de erreurs.

Le problème qui se pose maintenant est de savoir quoi afficher et où d’où l’objet de cet article.

## Logs dans une fonction unique

Par définition, une fonction reçoit en entrée aucun ou plusieurs paramètres, ensuite effectue des opérations et retourne un résultat.

<img src="./img/fr/1. architecture.png" alt="Architecture d'une fonction" width="100%" />

Dans une fonction simple les informations utiles à afficher dans les logs sont :

- Le(s) paramètre(s) que la fonction reçoit.
- Le résultat après opérations (optionnel utile quand on a une suite d’appel de fonctions).

Par exemple pour une fonction qui ne prend aucun paramètre et retourne le message ‘Hello’ on aurait en Python :

<img src="./img/fr/3. func_no_parameter.png" alt="Log d'une fonction sans paramètre" width="100%" />

Supposons que la fonction prenne en paramètre un nom et retourne « Hello nom d’utilisateur », on aurait :

<img src="./img/fr/4. func_with_parameter.png" alt="Log d'une fonction avec paramètres" width="100%" />

Si on veut afficher le résultat de la fonction dans les logs on aurait :

<img src="./img/fr/5. func_with_parameter_and_response.png" alt="Log d'une fonction avec paramètres et résultat" width="100%" />

**Quand les paramètres contiennent des informations confidentielles comme l’email et mot de passe, il ne faut pas afficher ces informations dans les logs il faut les remplacer par \*\*.**

## Logs dans une suite de fonctions

Un programme informatique est une suite de fonctions et méthodes qui s’appellent entres elles. Supposons un programme constitué de 3 fonctions _fonction A_,_fonction B_ et _fonction C_ avec la pile suivante :

<img src="./img/fr/2. architecture_multiple.png" alt="Architecture d''appel de plusieurs fonctions" width="100%" />

Quand on a plusieurs fonctions les logs doivent se présenter comme suit :

- La fonction appelante doit afficher ses paramètres lors de son appel.
- La fonction appelante après avoir exécuté une autre fonction doit afficher le résultat obtenu.
- La fonction appelante peut afficher le résultat renvoyé.

Soit une fonction main qui appelle une fonction obtenirNom et avec le nom saisi par l’utilisateur appelle une fonction hello pour afficher le message ‘Hello nom d’utilisateur’.

Si on veut appliquer les logs dans cette suite de fonctions on aurait :

<img src="./img/fr/6. func_multiple_call.png" alt="Log d'une suite de fonctions" width="100%" />

L’exécution donnerait :

<img src="./img/fr/7. example.png" alt="Log d'une suite de fonctions exécution" width="100%" />

**Dans les exemples précédents nous avons utilisé la fonction print pour afficher les logs. Dans vos projets il faut préférer des modules de logs de votre langage. En Python, vous pouvez utiliser [Logging](https://docs.python.org/3/library/logging.html).**

**Les techniques décrites plus haut reste adaptable selon vos besoins.**

**Quand les paramètres contiennent des informations confidentielles comme l’email et mot de passe, il ne faut pas afficher ces informations dans les logs il faut les remplacer par \*\*.**
