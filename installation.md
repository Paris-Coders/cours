# Installer Python

Ce premier tutoriel, que nous pourrions appeler tutoriel zéro, n'est qu'un simple tutoriel d'installation de Python.
Si vous avez déjà Python sur votre machine, ce tutoriel ne vous sera d'aucune utilité.

## Introduction

Python désigne deux choses :
* le langage de programmation ;
* un exécutable, appelé interpréteur, permettant de lire du code écrit en langage Python.

Afin de pouvoir travailler, il vous faut l'interpréteur Python, permettant ainsi de lire le code que vous allez l'écrire.
Autrement dit, vous allez pouvoir utiliser n'importe quel logiciel de texte (Bloc notes, Notepad++, gedit, kedit, Sublime Text...)
pour écrire votre code dans un fichier, fichier que sera ensuite lu par Python pour l'exécuter et produire le résultat.
Au final, pour lancer Python et lui dire de lire (d'exécuter) un fichier, il faudra faire ainsi :
```bash
	python nom_du_fichier.py
```
Par contre, il faudra le faire dans une invite de commande (aussi appelé terminal, sous Linux et Mac OS).

Heureusement, des éditeurs de code évolués effectuent cette commande pour vous en lui donnant en paramètre, le nom du fichier actuellement en cours d'édition. Toutefois, dans ce tutoriel, nous nous pencherons surtout sur une installation basique (de Python seulement), vous laissant ainsi le choix sur l'éditeur de code.

### Tester l'installation

Il suffit de taper :
```
	python
```
dans l'invite de commandes et vous verrez apparaître :
```
	Python 2.7.9 (default, Dec 29 2014, 06:44:46) 
	[GCC 4.8.3] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 
```
prouvant ainsi que Python est bien installé et accessible. Si ce n'était pas le cas, cela afficher une erreur du style `commande inconnue`.

### Notes supplémentaires

Durant ces cours, nous utilisons Python 2.7.


## Windows

### Méthode basique

* [https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi] (https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi) ;
* Installez le fichier téléchargé ;
* Cliquez deux fois sur `Next` ;
* Sur la page du choix des composants à installer, sélectionnez `Add python.exe to Path` ;

Voilà, c'est prêt.

### Méthode avec cygwin

Cygwin est un programme qui permet à différentes version de Windows, d'émuler Unix et donc d'avoir la multitude de commande et de programmes utiles au sein de Windows. 
Il faut télécharger Cygwin dans le lien suivant [https://cygwin.com/setup-x86.exe] (https://cygwin.com/setup-x86.exe). Durant l'installation, vous devez vous assurer d'installer :
* python
* wget
* svn

Si vous avez un quelconque problème ou doute, durant l'installation de cygwin, vous pouvez consulter [ce tutoriel] (https://forums.oneplus.net/threads/tuto-installation-cygwin-et-kitchen-par-konigtiger.214228/).

Suivez les instructions au pas à pas jusqu'à que vous lisiez cette phrase: **Je vous conseille vivement dans cette étape d'installer tout les packages disponible en cliquant sur "le cercle noir avec deux flèches inversée l'une de l'autre". Cliquez "Suivant"**

Comme vous pouvez le voir :
![sur l'image] (http://image.noelshack.com/fichiers/2014/51/1418924249-bandicam-2014-12-18-18-36-35-434.jpg)
il y'a un carré avec *search* 

Tapez les mots ci-dessous qui sont des packages dans le carré **Search** et assurez-vous qu'ils soient tous en mode **install** en cliquant sur l'icône de boucle.

- python
- wget
- svn

Vous avez désormais un émulateur linux.

Ouvrez une fenêtre bash en cliquant sur l'onglet *Cygwin Terminal* qui se trouve sur votre bureau.

Une fois la fenêtre ouverte, tapez ```python``` , Python devrait bien avoir été installé.

## Linux 

Dans de nombreuses distributions, Python est installé par défaut.
Si ce n'est pas le cas, il suffit d'utiliser le gestionnaire de paquet et d'installer Python (2.7). Si vous n'avez aucune idée de tout cela, veuillez vous référer à la documentation officielle de votre distribution.

Pour lancer Python, il suffira d'ouvrir un `terminal` et de taper `python`.

## Mac OS X

Pour trouver le terminal, utilisez [la recherche] (https://www.youtube.com/watch?v=zw7Nd67_aFw) et tapez `terminal`.
Cela ouvre une nouvelle fenêtre dans laquelle vous pouvez taper `python` pour lancer Python.
Si celui-ci n'est pas installer, insérez la commande suivante pour l'installer :
```
	brew install python
```
(La commande vous demandera votre mot de passe, sans quoi elle ne peut faire l'installation.)




