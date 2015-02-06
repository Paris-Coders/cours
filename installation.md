# Installer Python

Ce premier tutoriel, que nous pourrions appeler tutoriel zéro, n'est qu'un simple tutoriel d'installation de Python.
Si vous avez déjà Python sur votre machine, celui-ci ne vous sera d'aucune utilité.

## Introduction

Python désigne deux choses :
* le langage de programmation ;
* un exécutable, permettant de lire du code écrit en langage Python.

Afin de pouvoir travailler, il vous faut cet exécutable Python, permettant ainsi de lire le code que vous allez l'écrire.
Autrement dit, vous allez pouvoir utiliser n'importe quel logiciel de texte (Bloc notes, Notepad++, gedit, kedit, Sublime Text...)
pour écrire votre code dans un fichier, fichier que sera ensuite lu par Python pour l'exécuter et produire le résultat.
Au final, pour lancer Python et lui dire de lire (d'exécuter) un fichier, il faudra faire ainsi :
```bash
	python nom_du_fichier.py
```
Par contre, il faudra le faire dans une invite de commande (aussi appelé terminal).

Heureusement, des éditeurs de code évolués effectuent cette commande pour vous. Toutefois, dans ce tutoriel, nous nous pencherons surtout sur une installation basique (de Python seulement), vous laissant ainsi le choix sur l'éditeur de code.

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

* [https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi]https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi) ;
* Installez le fichier téléchargé ;
* Cliquez deux fois sur `Next` ;
* Sur la page du choix des composants à installer, sélectionnez `Add python.exe to Path` ;

Voilà, c'est prêt.

### Méthode avec cygwin

Cygwin est un programme qui permet à différentes version de Windows, d'émuler Unix. Il faut télécharger Cygwin 
dans le lien suivant [https://cygwin.com/setup-x86.exe] (https://cygwin.com/setup-x86.exe)


## Mac OS X

## Linux

La bonne nouvelle : il est installé de base.
Si ce n'était pas le cas, utilisez votre gestionnaire de paquets et cherchez python 2, afin de l'installer.


