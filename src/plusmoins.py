#!/usr/bin/python
# La ligne ci-dessus est speciale et utilisee par Linux. 
# Elle indique qu'elle est l'interpreteur a utiliser pour lire le fichier
#
# Les lignes commencant par '#' sont des commentaires. Ils sont totalement
# ignores par Python et nous permettent ainsi de donner des indication sur
# le code.

from random import randint

secret = randint(1,100)

choix = -1	# Ceci permet de definir la variable choix (sinon, Python indiquera
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
