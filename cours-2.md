# Introduction

Ce cours porte sur :

  *  les commentaires dans le code
  *  les fonctions
  *  le jeu des allumettes

# Les commentaires 

Je n'en avais pas parlé la première fois et je trouve cela très dommage car les commentaires sont vraiment importants dans le code. Les commentaires, ce sont des lignes que Python ne prendra pas en compte. Ainsi, vous pouvez écrire tout ce que souhaitez :
```python
    # Mon super commentaire d'exemple
```

Cette ligne, bien qu'insérée dans notre code, ne sera pas prise en compte par Python (elle est ignorée, tout simplement). Par contre, il est intéressant de placer ce genre de ligne, car vous pouvez ainsi mieux décrire ce que fait le code que vous avez écrit. En effet, lorsque vous aller relire votre code dans quelques mois, vous n'allez pas vous rappeler de ce que vous avez pensé en écrivant le code et ... vous n'allez pas le comprendre en le lisant. Ne vous inquiétez pas, cela arrive à tout le monde. De plus, vous pouvez aussi partager votre code (ou avoir à le montrer à quelqu'un d'autre, pour qu'il vous aide) et donc, celui-ci pour comprendre rapidement votre code, pourra lire les commentaires.
Avec le caractère `#` vous ne pouvez que commenter sur une ligne, ce qui peut ne pas être très pratique. Pour commenter sur plusieurs lignes, vous pouvez utiliser trois guillemets ("""). Voici un exemple :
    
```python
    """
    Ma fonction affiche le plan du métro dans une nouvelle fenêtre
    Pour cela, elle charge un fichier, puis ouvre une fenêtre et affiche le plan
    """
    def afficherPlan():
        ...
        ...
```

Attention ! Vos commentaires ne doivent pas dire en français exactement ce que fait la ligne :

```python
    i=i+1 # Incrémente le compteur i
```

Car là, c'est totalement inutile (c'est redondant). Le code est lisible et le lecteur comprend en lisant le code que vous incrémenter la variable i.
Par contre, si votre variable i, permet de passer à la prochaine case d'un tableau, vous pouvez mettre :

```python
    i=i+1 # On avance d'une case pour continuer l'algorithme
```

(Même si là, ce n'est pas très très utile, mais c'est pour l'exemple.)

Pour le moment, nous n'avons pas vraiment eu besoin des commentaires, car nous avons fait l'algorithme au tableau de nos programme, tous ensemble. Mais, un jour viendra ou je vais vous laisser faire l'algorithme seul et pour comprendre comment vous avez conçu votre programme, j'aurais besoin d'une explication avec les commentaires.


# Les fonctions

Au fur et à mesure, nos programmes vont devenir plus complexe. Ce n'est pas un réel soucis, par contre, nous devons l'organiser. Si vous voulez, on peut comparer cela à une bibliothèque. Actuellement, nous avons deux livres et c'était facile de s'y retrouver. Mais bientôt, nous aurons des centaines de livres et, pour les retrouver facilement, nous les rangeons par ordre alphabétique. Au final, un programme c'est pareil. Il va savoir faire de plus en plus de choses (afficher des données, se connecter à un site web, jouer un son ...) et chacune de ces tâches, nous allons en faire une fonction. D'une part, cela nous évitera de copier coller le code pour jouer un son, à chaque fois que nous voulons jouer un son, mais en plus, cela permettra d'organiser le programme.

Par exemple, si un jour, vous remarquez qu'il y a un soucis avec votre fonction pour jouer un son, vous corrigez la fonction qui joue un son et hop, quelque soit l'endroit (dans le programme) où le son est joué, la fonction corrigée est appelée. Si on avait fait un copier-coller (chose qui devrait être interdite en programmation), il aurait fallu corriger le code autant de fois qu'il aurait été copier. Et je peux vous dire, par expérience, on oublie toujours un endroit.

Bref, pour les fonctions, Python introduit un nouveau mot clé : def. Il permet d'indiquer que l'on va faire une fonction, comme suit :
    
```python
    def maFonction():
        print "Ma fonction trop utile"

    # Et pour l'appeler 
    maFonction()
```

Le fait d'appeler une fonction, fait que le programmation va d'abord exécuter le code dans la fonction, avant de continuer d'executer la suite linéaire du programme.
Si j'écris :

```python
    print "1"
    maFonction()
    print "2"
```

Le programme affichera :
    1
Ma fonction trop utile
    2


Deux particularités. Une fonction peut prendre des paramètres. Ce sont des variables qui seront utilisés dans la fonction et qui provienne du moment où la fonction est appelée :

```python
    def afficheBonjour(nombre):
        i=0
        while(i<nombre):
            print 'Bonjour'
            i=i+1

    afficheBonjour(5)
```

Ici, on affiche cinq fois bonjour. Mais si un jour, je veux afficher dix fois bonjour, j'ai simplement à lui donner en paramètre 10.

Par contre, il est important de noter que les paramètres sont copiés :

```python
    def maFonction(toto):
        print 'Ma fonction'
        toto=toto+1
   
    titi=42
    maFonction(titi)
    print titi
```

    Ceci affiche
    Ma fonction
    42

Car, la variable `toto` dans la fonction `maFonction()` est locale et elle n'existe que dans la fonction. En réalité, cette variable toto, contient une copie du contenu de la variable titi passée lors de l'appel de la fonction. Cette variable toto n'existe plus lors de la fin de la fonction.
La seconde particularité est qu'une fonction peut retourner une valeur :

```python
    def donneNombre():
        return 42
```

Pour indiquer la valeur à retourner, il faut utiliser le mot clé return. Ici, je peux faire :

```python
    toto = donneNombre()
    print toto
```

Ce qui affichera 42.

# Le jeu des allumettes

Le jeu des allumettes est connu, notamment car il était utilisé dans une des épreuves de réflexion de Fort Boyard.
C'est un jeu à deux joueurs. Dans notre cas, la machine ne fait que gérer le jeu (une sorte d'arbitre).
Quinze allumettes sont posées sur la table. Chaque joueur joue à tour de rôle. Chaque joueur peut prendre soit 1, 2 ou 3 allumettes. Le joueur qui prend la dernière allumette a perdu.

Il faut comprendre que les allumettes ce sont des choses qui n'existent pas réellement dans un PC. En réalité, ce qui nous intéresse, ce n'est pas vraiment que ce sont des allumettes, mais simplement, leur nombre. Du coup, on va juste utiliser une variable contenant, le nombre d'allumettes. Ensuite, il n'y a pas vraiment de chose compliquée :

    nombreAllumettes = 15

    Tant qu'il y a des allumettes
        Afficher nombre allumettes
        choix = demander nombre allumettes prises
        if choix >= 1 ET choix <= 3
            nombreAllumettes = nombreAllumettes - choix

    Afficher défaite


Ce qui nous donnera, en code :

```python
    nombreAllumettes = 15
    while nombreAllumettes > 0:
        print "Il y a " + str(nombreAllumettes) + " sur la table"
        choix = input()
        if choix >= 1 and choix <= 3:
            nombreAllumettes = nombreAllumettes - choix

    print "Vous avez perdu"
```

Ici, il y a tout de même des particularités.
Déjà, le while. Nous ne faisons pas un simple != 0, car si le joueur prend 2 allumettes alors qu'il y en restait une, le programme verrait que nombreAllumettes = -1, ce qui est également différent de zéro, et il continuerai indéfiniment.

De plus, ici, nous voyons comment faire deux tests avec un seul if. En réalité, on peut mettre autant de condition que nous souhaitons, mais celles-ci doivent être lié par un opérateur logique :

    ET (and)
    OU (or)

Ainsi :

```python
    if cond1 and cond2:
```

Ne sera vrai que si la condition 1 ET la condition 2 seront valides.
    
```python
    if cond1 or cond2:
```

Ne sera vrai si l'une ou l'autre des condition est validée.

Dernier point, dans le code du jeu, c'est la concaténation de chaîne de caractères.
Vous pouvez toujours écrire :
   
```python 
    print "Mon " + "code " + "est "  + "super"
```

Le '+' indique à Python qu'il devra concaténer (mettre bout à bout) les différentes chaines de caractère.
Par contre, si vous essayez avec un nombre :

```python
    print "J'ai " + 42 + " allumettes"
```

Cela vous donnera une erreur. En effet, il ne peux pas mettre bout à bout, une chaine de caractère et un nombre. Par contre, on peut lui dire de transformer le nombre en une chaine de caractère. C'est ce que fait la fonction str().

```python
    print "J'ai " + str(42) + " allumettes"
```

Ici, `str(42)`, retourne la chaine de caractères "42" (qui est composée du caractère 4 et du caractère 2). Il faut bien comprendre la différence. En effet, 42, c'est un nombre, sur lequel vous pouvez faire des opérations arithmétiques classiques (additions, multiplications...). "42" est une chaine de caractère (un ensemble de caractère). Vous ne pouvez pas faire d'addition avec, par contre, vous pouvez appliquer les fonctions sur les chaines de caractères.

J'espère que c'est clair, en tout cas, n'hésitez pas à demander des précisions ou des explications supplémentaires.

# Exercices

Notre jeu des allumettes, il est assez nul. Vous pouvez l'améliorer et je vous sollicite à le faire et à nous montrer vos améliorations. Parmi celles-ci, vous pouvez :

  *  Afficher joueur1/joueur2 et afficher le joueur qui a gagné
  *  Faire jouer l'ordinateur en tant que joueur 2 :) (pour le début il prendra un nombre aléatoire d'allumettes, voir le cours précédent ;) )
  *  Trouver une méthode pour gagner à 100 % et l'implémenter pour que l'ordinateur l'utilise (c'est simple, c'est une méthode mathématique).
