# Introduction

Ce cours vise les débutants qui veulent apprendre la programmation et cela, rapidement. Tous les aspects ne seront pas abordés, mais la logique, à la base de tout programme y est enseigné et c'est celle-ci, qui vous suivra tout au long de votre vie de programmeur.

Le premier cours porte sur les points suivants :

 * la différence entre les langages compilés et les langages interprétés ;
 * quelques bonnes pratiques en programmation ;
 * un exercice à résoudre.

# Les langages de programmation

Python est un langage de script, ou, pour être plus précis, un langage interprété. En programmation, nous avons deux grandes classes de langage : les langages interprétés (Perl, Python, Ruby...) et les langages compilés (C, C++, ...).

En réalité, votre ordinateur ne comprend que des zéros et des uns. Lorsque vous écrivez un programme, avec n'importe quel langage de programmation, il y a une étape de traduction, qui transforme votre code source en code machine (du binaire, que la machine peut vraiment traiter).
Pour un langage compilé, cette transformation s'effectue à l'aide d'un compilateur, qui va analyser votre code, le transformer et l'optimiser. Le compilateur va produire un exécutable qui pourra être lancé.
Pour un langage interprété, cette transformation est effectuée par un interpréteur (la commande python, dans notre cas), qui va lire le fichier et pour chaque ligne que vous avez écrit, il va faire l'action associée (qui elle a été préparée et est compréhensible par la machine). Cette interprétation n'est pas gardée. Cela veut dire que si vous relancez votre programme, il va refaire l'interprétation.

Chacune des deux classes possèdent ses avantages. Les langages compilés sont généralement plus rapides. Les langages interprétés peuvent être utilisé comme langage de script, où vous pouvez taper vos commandes une part une et l'ordinateur fera l'action associée. En effet, si vous lancez "python" dans une ligne de commande (ou terminal), il va vous afficher une invite ">>>" et vous pourrez directement insérer votre code qui sera interprété au fur et à mesure.


# Quelques bonnes pratiques en programmation

Je vous conseille de vous organiser. Au fur et à mesure de ce cours nous allons faire des exercices. Mon conseil est donc de ne pas mettre vos fichiers de code sur le bureau, ou dans vos Documents, mais de créer une arborescence un peu plus organisée. Celle que je propose est la suivante :

 * Un nouveau dossier "Developpement"
 * Un sous dossier "Python" (ou pour tout autre langage que vous voulez découvrir :))
 * Des sous dossier pour chaque exercice "Cours1"/"Cours2"/...


Sachez qu'un exercice peut contenir plusieurs fichiers, ou chaque fichiers contiendra du code spécifique à telle ou telle action. Mais, nous découvrirons cela plus tard.
Bien sur, vous êtes libre de faire comme vous souhaitez. Mais il est toujours bon de bien s'organiser dès le début.


Maintenant, parlons un peu plus de ce qui se trouve dans un fichier de code.
En programmation, nous tenons absolument à une chose : [l'indentation](http://fr.wikipedia.org/wiki/Style_d%27indentation). En Python, elle est obligatoire (et c'est le seul langage qui force une telle chose).
L'indentation, c'est le fait de ce décaler vers la droite, pour écrire son code. On peut indenter son code avec la touche "Tabulation", celle au dessus du verrouillages des majuscules (la touche avec le cadenas).
La règle est d'indenter le code qui sera exécuter par les conditions, ou les boucles. En algorithme, cela donne :

```
Tant que la souris se cache
    le chat attend
Si la souris voit le chat
    la souris se cache
```

Tant que représente une boucle, et Si une condition. Ici, on voit que le chat attend, tant que la souris se cache. C'est pour cela que la ligne est indenté. Car dès que le Tant que ne sera plus valide, on ne va plus exécuter "Le chat attend". Il en est de même pour la condition. Si la souris voit le chat, alors la ligne "La souris se cache" sera exécutée. Grâce à l'indentation, cela est visible dès le premier coup d'oeil. Si vous aviez mis tout sur la même colonne, alors vous aurez du lire le code intégralement pour vous y retrouver. Pire encore, en programmation, il arrive très souvent (et cela, dès notre premier exercice) d'avoir des tests (conditions), imbriqué dans des boucles. Du coup, on va utiliser deux niveaux de décalage :
```
Tant que ...
    Si ...
        Action
```

On voit immédiatement que l'action dépend du `Si`, qui dépend du `Tant que`.
En Python, si vous ne respectez pas l'indentation, c'est tout le fonctionnement du programme qui change. En effet, Python utilise l'indentation pour savoir si telle ou telle ligne est comprise dans l'action du si (ou du Tant que). Si vous oubliez d'indenter le code après un Si (ou autre boucle/test), alors il vous indiquera : Indentation Error (erreur d'indentation).

En programmation, nous avons aussi les variables. Une variable permet à l'ordinateur de retenir une information. Si vous avez fait les exercices de Codecademy, vous avez sûrement déjà saisi cela. Toutefois, le nommage des variables (et des fonctions et des classes... (que nous verrons plus tard)) est très important. En effet, encore une fois, cela joue sur la lisibilité de votre code.
Une variable doit avoir un nom clair et concis. Si vous voulez stocker le résultat d'une opération (par exemple, une addition), vous pouvez appeler la variable "resultat". Mais si en plus de cela, vous savez que le résultat de l'opération, c'est le prix d'une voiture, alors il sera encore plus clair de l'appeler "prixVoiture" (ou prix).
Notez ici, que j'ai utilisé l'écriture "prixVoiture" et non prixvoiture. Cela s'appelle la notation CamelCase, qui permet de bien séparer les mots dans le nom de la variable, grâce aux majuscules (en effet, l'espace n'est pas utilisable, sinon le langage comprendra que c'est un autre mot).
En conclusion, utilisez des noms de variables clair et concis. Pas besoin d'écrire un roman comme : "maSuperVariableQuiContientMonSuperResultat", ni d'écrire juste "a", puis "b", puis "c" ... car le premier exemple est trop long à écrire (et les programmeurs sont généralement un peu feignant) et les autres exemples n'indique en rien le but de la variable. 

Vous vous demandez pourquoi tout ces conseils ? Simplement car vous n'êtes pas le seul à lire le code. Un collègue peut lire votre code, ou encore plus simplement, votre camarade dans votre groupe. Mais pire encore, si vous revenez sur votre code, même pas un mois après l'avoir écrit, il y a de très grande chance que vous ne vous rappeliez pas de ce que vous avez voulu faire. C'est pour cela que le code doit vraiment être clair.


# Exercice

Passons à l'exercice. Vous allez voir, il est loin d'être complexe. En effet, nous allons utiliser que trois notions de la programmation (et de Python) : les variables, les conditions et les boucles.

Nous allons programmer le jeu du plus ou moins. Ce jeu peut se joue généralement à deux. Voici son déroulement :

 * Joueur A choisit un nombre entre 1 et 100 ;
 * Joueur B donne un nombre à Joueur A ;
 * Joueur A indique si son nombre est plus grand, ou plus petit, ou encore, si Joueur B a trouvé le nombre ;
 * Le jeu continue jusqu'à ce que le Joueur B trouve le nombre (ou encore, jusqu'à qu'ils en aient marre :D).

De cette explication, nous allons en tirer l'algorithme. L'algorithme, c'est une description en français (ou autre) de comment l'ordinateur doit agir. Ici, on ne parle pas encore de programmation, ni de rien qui est lié à la machine. Voici le premier algorithme (incomplet) :

```
    Prends un nombre "au hasard" entre 1 et 100 (on parle d'aléatoire, en informatique) (appelé secret) ;
  
    Demande un nombre à l'utilisateur (appelé choix)
    Si choix est égal à secret
        Affiche "bravo"
    Si choix est inférieur à secret
        Affiche "plus grand"
    Si choix est supérieur à secret
        Affiche "plus petit"
```

Ok, mais si vous regardez bien, ce n'est suffisant. En effet, ici, on ne demande qu'une seule fois le nombre à l'utilisateur, même s'il n'a pas gagné. Il faut donc une boucle, pour le faire jouer plusieurs fois :

```
    Prends un nombre "au hasard" entre 1 et 100 (on parle d'aléatoire, en informatique) (appelé secret) ;
     
    Tant que choix est différent de secret
        Demande un nombre à l'utilisateur (appelé choix)
        Si choix est égal à secret
            Affiche "bravo"
        Si choix est inférieur à secret
            Affiche "plus grand"
        Si choix est supérieur à secret
            Affiche "plus petit"
```

(On remarque que j'indente bien mon algorithme)

Bon, j'ai été un peu vite, je l'avoue. N'hésitez pas à poser des questions si vous ne comprenez pas. Pire ! Pendant la séance, je n'avais pas exactement fait l'algorithme de cette façon. Bref, cela me permet de dire : À un problème (ici, celui de faire le jeu du plus ou moins), vous pouvez avoir plusieurs solutions. Rien ne vous oblige de suivre parfaitement ma solution, tant que vous arrivez au résultat. Toutefois, on cherchera souvent la solution la plus immédiate, la moins contraignante, la plus logique et efficace.


## Implémentation

Il ne reste qu'une étape. Traduire cet algorithme en code Python. Vraiment, ici, vous avez fait l'équivalent de 75 % du travail. Il ne reste plus qu'à ouvrir l'éditeur de code, votre fichier .py (les fichiers Python par convention s'appelle .py) et à remplace les mots français de l'algorithme par les mots clés de Python.

Il y a deux particularités que je vais tout de même vous donner ici :

    Pour que l'ordinateur puisse prendre un nombre aléatoire (entre 1 et 100), il faut écrire :
```python
        from random import randint
        randint(1,100)
```
    Pour que l'ordinateur demande à l'utilisateur d'entrée un nombre :
```python
        input()
```

La ligne "from random import randint" indique à Python, que dans notre code, nous voulons utiliser la fonction randint(). Celle-ci n'est pas disponible par défaut. Elle se trouve dans une boite à outils (module). Donc, on indique clairement à Python : "Dans le module random, importe la fonction randint()". Ainsi, dans le reste du code, vous pouvez utiliser la fonction randint(). Au fur et à mesure, nous verrons sûrement d'autres modules pour faire des choses encore plus avancées.

Note : l'importation de module se fait toujours au début du fichier.

Voici le [code final]() :

```python
	#!/usr/bin/python
	# La ligne ci-dessus est speciale et utilisee par Linux.
	# Elle indique qu'elle est l'interpreteur a utiliser pour lire le fichier
	#
	# Les lignes commencant par '#' sont des commentaires. Ils sont totalement
	# ignores par Python et nous permettent ainsi de donner des indication sur
	# le code.

	from random import randint

	secret = randint(1,100)

	choix = -1  # Ceci permet de definir la variable choix (sinon, Python indiquera
				# une erreur pour la ligne ci dessous, car choix n'existe pas)
				# La valeur de -1, permet d'etre sur de ne jamais etre egal a secret
	while choix != secret:
		print "Entrez votre nombre : "
		choix = input()
		if choix == secret:
			print "Bravo"
		if choix < secret:
			print "Plus grand"
		if choix > secret:
			print "Plus petit"
```

## Aller plus loin

Voilà. Si vous voulez aller plus loin. Vous pouvez essayer d'ajouter un nombre de tour à ne pas dépasser, sinon, le joueur perd (et on lui afficher un message de perte).
