# Propreté du code

Je tiens à redire qu'il est important de bien nommer les variables et les fonctions que vous créez. En effet, c'est en les nommant correctement et en leur donnant un nom explicite par rapport à leur tâche que vous allez plus facilement vous repérer dans le code.
Un deuxième point que j'ai énoncé durant le cours était à propos de notre code des deux jeux précédents : le jeu du plus-moins et le jeu des allumettes. Nous avions utiliser la fonction "input()" afin de récupérer la valeur entrée par l'utilisateur.
Si vous avez été curieux et que vous aviez entrer une lettre ou un mot, le programme plantait.
En informatique, il ne faut jamais faire confiance en l'utilisateur. Dans le sens, si vous lui laissez la possibilité de rentrer des informations, il va très certainement insérer des informations incorrecte (sur les sites web, cela mène à des piratages, sur les programmes normaux, cela mène à des crash, mais un crash peut mener aussi à un piratage). Ici, nous voulions un nombre, alors, il faut vérifier qu'il rentre bien un nombre. Par exemple, nous pouvons le faire avec la fonction int(). Elle permet de transformer la chaine de caractères en entrée, pour nous retourner un nombre. Si la chaine de caractères n'est pas transformables, alors, int() lance une exception. De plus, la fonction input(), n'est pas la meilleure pour les entrées utilisateurs. raw_input() est bien mieux et va nous permettre de correctement gérer les lettres et les mots, dont nous aurons besoin dans le jeu du pendu.

# Les exceptions

Je vous en parlais juste précédemment. int() est une fonction qui peut lancer une exception.
Lorsqu'une exception est envoyée, le programme va retourner dans la fonction parente (ou appelante). Si celle-ci (l'exception) est attrapée, alors l'exécution du programme va continuer là où l'exception est envoyée, sinon, elle va être transférée à la fonction parente (et ainsi de suite). Au bout d'un moment, on va revenir à la fonction la plus parente (la fonction globale au programme). Si elle n'est toujours pas attrapée, alors le programme s'arrête.
Voici un programme simple, envoyant une exception qui n'est pas attrapée :
var = int("Blah")

Voici ce que le programme affiche :
    Traceback (most recent call last):
      File "./test.py", line 1, in <module>
        var = int("Blah")
    ValueError: invalid literal for int() with base 10: 'Blah'

Les trois premières lignes indiquent le "Traceback", qui est un suivi du chemin fait par l'exception lorsqu'elle remonte les fonctions. À chaque niveau, cela va afficher le nom du fichier, la ligne, le module, puis la ligne en question. Ainsi, vous pouvez voir d'où vient l'exception et ainsi essayer de corriger le souci.
La dernière ligne indique la raison de l'exception (pourquoi elle a été lancée).

Notez qu'un programme qui n'attrape pas ses exceptions est un mauvais programme, car il va s'arrêter sans préavis. En effet, un programme qui s'arrête brutalement, c'est un programme qui ne sauvegarde pas les données de l'utilisateur. Imaginez l'utilisateur qui travaille toute la journée et le soir, le programme plante sans sauvegarder le travail. Je peux vous assurer que l'utilisateur voudra votre mort après ça.

Voyons donc, comment attraper les exceptions. Pour cela, nous allons introduire un nouveau "bloc", délimité par le mot clé try. 
Il permet de dire que le code qui va être exécuté est susceptible de lancer une exception :

    try:
        var = int("Blah")

Soit. Mais nous n'indiquons pas encore que nous souhaitons attraper une exception. Pour cela, nous avons un autre bloc, introduit par le mot clé except. Plus précisément, il faut indiquer à Python quelle exception vous souhaitez attraper :
    try:
       var = int("Blah")
    except Exception:
       print "Erreur du programme"

L'exception va être lancée par int(). Aucun problème, nous avons intégré l'appel à la fonction, dans un bloc try et nous attrapons les exceptions "Exception". Du coup, ici, le programme va afficher "Erreur du programme". C'est bien mieux, car dans ce bloc except, vous pouvez sauvegarder le travail de l'utilisateur par exemple.
Vous pouvez mettre autant de bloc except que vous souhaitez, afin de spécialiser votre message d'erreur (ou plus généralement, la réaction du programme fasse à l'erreur) :
    try:
       var = int("Blah")
    except ValueError:
       print "Impossible de convertir"
    except Exception:
       print "Erreur inconnue"

Ici, dans le cas d'une ValueError (retournée par int()), j'affiche le message approprié. De même, nous pourrions redemander à l'utilisateur d'entrer un nouveau nombre vu que le programme à remarquer qu'il faisait une chose incorrecte.
Par contre, dans le cas où ce n'est pas une ValueError, le message affiché sera "Erreur inconnue". On peut imaginer, que nous fermons le programme et, si on le veut, on pourrait envoyer un message au programmeur pour lui dire que quelque chose ne vas pas. Tout est imaginable.

Notez que j'ai bien pris la précaution de mettre le cas spécialisé avant le cas généraliste. En effet, Exception toute les exceptions Python sont des Exception (le type). Si j'indique que je souhaite attraper les Exception (cas généraliste) avant d'attraper la ValueError (cas spécifique), alors jamais le programme n'affichera le message "Impossible de convertir" car l'exception se ferait attraper par le cas généraliste.

Il existe un raccourci, pour indiquer le cas généraliste :
    try:
       var = int("Blah")
    except ValueError:
       print "Impossible de convertir"
    except:
       print "Erreur inconnue"

Simplement. Ce code fait la même chose.

Il existe un dernier mot clé : finally. Celui ci définit un bloc, qui sera exécuté à la fin du bloc try, que l'exception ait 
lieu ou non.

    try:
       var = int("Blah")
    except ValueError:
       print "Impossible de convertir"
    except Exception:
       print "Erreur inconnue"
    finally:
       print "Programme fini"

Dans tous les cas, mon programme affichera "Programme fini".

    Mots de fin sur les exceptions


Vous pouvez vous même lancer une exception en utilisant le mot clé raise :

    def buggyFunction():
       raise IOError()

    try:
       buggyFunction()
    except ValueError:
       print "Impossible de convertir"
    except Exception:
       print "Erreur inconnue"
    finally:
       print "Programme fini"

Vous pouvez aussi définir vos propres type d'exceptions. Je ne l'ai pas décrit durant le cours, car cela ne me semblait pas utile pour le moment.


# La documentation

Vous pouvez vous demander comment j'ai su que la fonction int() peut envoyer une exception. En programmation, il n'y a pas de magie, ni de hasard. Si la fonction int() renvoie une exception, c'est que son créateur a voulu que ce soit le cas. Mais, le créateur a été très gentil, il a aussi écrit une documentation indiquant que cela se passait ainsi et décrivant aussi, le fonctionnement de la fonction. Pour la fonction int(), vous pouvez trouver la documentation (officielle) ici : https://docs.python.org/2/library/functions.html#int
Chaque fonction, qu'elle provienne d'un module, ou du langage est documentée. Je vous conseille vivement de toujours vous référer à la documentation. Si vous avez un doute, allez voir la documentation. Si vous ne connaissez pas une fonction, allez voir la documentation. C'est ainsi que les programmeurs font.

Si vous avez une question, ou un souci pour faire un truc, n'hésitez pas à demander à Google. Il suffit de taper "Python" 
avec quelques mots clés de votre phrase. Par exemple, comment convertir une chaine de caractères en nombre en Python :

    convertir chaine en nombre Python

ou encore 

    convert string to int Python


# Les listes

Python est un langage de haut niveau qui propose, de base, différentes structure de données (des structures pour organiser les données dans la mémoire de l'ordinateur). Parmi celles ci, nous avons les listes. Les listes, ce sont comme des tableaux permettant de placer une suite d'éléments.
Voici comment définir une variable de type liste :

    maListe = []

Si vous voulez ajouter un élément, vous pouvez utiliser append() qui rajoute un élément à la fin de la liste.

    maListe.append(42)

Vous pouvez aussi définir une liste avec une série d'éléments, dès la déclaration de la variable :

    maList = [42, 32, 22, 11]

Vous pouvez accéder à un élément de la liste, en utilisant un index (son emplacement dans la liste) :

    print maList[2] # affichera 22

Notez qu'un ordinateur compte toujours à partir de 0.

Python propose une série de fonctions pouvant travailler sur les listes. Vous les retrouverez, dans la documentation bien sur : https://docs.python.org/2/tutorial/datastructures.html


# Les dictionnaires

Les dictionnaires sont des structures de données où les données sont associées par une clé. Tout comme un dictionnaire, pour un mot (une clé), on a une définition (une valeur).
Pour définir un dictionnaire vide, nous pouvons faire :

    monDict = {}

Pour le remplir, vous pouvez lui indiquer une clé et sa valeur ainsi :

    monDict["Age"] = 42

Si la clé existe déjà, la valeur lui correspondant sera simplement écrasée par la nouvelle.
Vous pouvez définir un dictionnaire, avec une multitude d'éléments :

    popFrance = {
        "Paris" : 2211000,
        "Marseille" : 851420
    }

Comme pour les listes, il y a une série de fonctions pour les dictionnaires : https://docs.python.org/2/tutorial/datastructures.html#dictionaries


# Les boucles for

J'avais parlé des boucles while, mais jamais des boucles for. En Python, les boucles for on un comportement proche des boucles "for_each" (pour chaque) des autres langages.
En effet, une boucle for, permet de passer sur chaque élément d'une structure.
Si vous voulez afficher chaque élément d'une liste, vous pouvez donc faire :

    for elem in maList:
        print elem

Si vous voulez faire la somme des élément de votre liste, de la même manière, vous pouvez faire :
somme=0
    
    for nombre in maListeDeNombre:
        somme = somme + nombre

Pour un dictionnaire, le principe est le même. Sauf que pour chaque tour de la boucle for, le dictionnaire vous retourne la paire clé/valeur :

    for clef,valeur in monDict:
        print clef + " -> " + valeur


# Algorithme du jeu du pendu

J'avoue, je ne pensais pas que la réalisation de ce jeu allait être aussi problématique. Mais vous allez voir, avec la bonne approche, il peut devenir très simple.
Pour rappel, le jeu du pendu est un à jeu à deux joueurs (ou plus) où l'on doit deviner/trouver un mot en proposant les lettres le composant. Au bout de N essais, on a perdu.

Pour cet exercice, je souhaiterai que vous placiez des commentaires et au moins, une fonction.

Essayons maintenant de trouver l'algorithme.

    trouver/choisir un mot
    Tant que le mot n'est pas trouvé, et que le nombre d'essais est un inférieur à 10, nous jouons
    Demande une lettre à l'utilisateur
    Cherche si cette lettre est présente dans le mot
        Si oui, faire apparaitre les lettres trouvées
        Si non, ne rien faire
    Afficher le mot caché

Bon, c'est encore vague, mais on a une meilleure décomposition. Essayons de résoudre les taches, une part une.

# Choisir un mot

Nous pourrions lire les mots à partir d'un fichier contenant tous les mots du français. C'est vrai, mais nous n'avons pas vu comment lire un fichier. Donc, on va faire plus simple (ou pourrait très bien lire un fichier par la suite :P). On va mettre quelques mots dans une liste et on va en prendre un.
Ok, mais comment en prendre un aléatoirement ?
Comme je l'ai dit dans le cours, vous pouvez accéder à un élément de la liste grâce à un nombre (que l'on appelle index).
Il suffirait donc de prendre un nombre aléatoire et de l'utiliser pour accéder à un mot de la liste.
Récupérer un nombre aléatoire, cela a été vu dans le premier jeu (celui du plus ou moins).
Ensuite, le reste ne sont que des opérations simples qui ont été vues dans le cours.
Une fois le mot choisi, je vous le conseille de le mettre dans une variable "motChoisi".

Notez que pour connaitre la taille d'une liste, vous pouvez utiliser la fonction len().

    len(maListe)

Le mot caché

Second indice et grande astuce pour cet exercice. Vous pouvez faire en sorte d'avoir une variable contenant des étoiles :
Par exemple, au début, pour le mot choisi "chien" , on aurait la variable cachée : "*****". 
Chaque fois qu'une lettre est entrée et qu'elle correspond au mot choisi, vous pouvez copier la lettre dans la variable cachée, 
ce qui fera que vous dévoilée peu à peu le mot.

Bon, cela peut ne pas être très clair, n'hésitez pas à demander des précisions.

Parcourir un mot

Pour parcourir un mot, lettre par lettre, vous pouvez aussi utiliser une boucle for :
    
    for lettre in mot:
        print lettre

Qui va vous afficher le mot, lettre par lettre.

Récupérer une lettre de l'utilisateur

Ici, nous devons utiliser raw_input() et non input(), car input n'est pas très bien pour récupérer des lettres 
(cela ne fonctionnera pas sans gêne).


Donc, pour revenir sur le principe général. C'est que nous aurons une variable contenant le mot choisi par l'ordinateur. 
Une seconde variable, qui contient le mot mais de façon caché (donc au début, que des étoiles). 

Au fur et à mesure que l'utilisateur donne des lettres, si elle corresponde au mot choisir, alors on les copient dans 
le mot caché, faisant apparaitre le mot peu à peu. Voilà, c'est tout. Il n'y a pas besoin de plus.

