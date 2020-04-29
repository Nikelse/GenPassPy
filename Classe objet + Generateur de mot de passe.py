# programmation orientée objet
# exemple de classe pour la generation de mot de passe simple
# NF.NSI

# classe generatrice de nombre aleatoire
import random

# creation de la classe
class MotDePasse :

    # DONNEES MEMBRES
    #__________________________________________________________________________

    # declaration des données membres
    taille = 40

    # caractere utilisé pour la generation
    char = "23456789abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ#&?!"

    # CONSTRUCTEUR
    #__________________________________________________________________________
    # lancé automatiquement lors de l appel de la classe
    # le mot clef self permet d'utiliser les données membres de la classe dont elle se réfère
    def __init__ (self) :

        self.Generateur()

    # FONCTIONS MEMBRES
    #__________________________________________________________________________
    def Generateur (self) :

        # variable pour stocker le mot de passe concatené
        code = ""

        # le code doit etre composé de %taille% caratere
        for compteur in range(0, self.taille) :

            # index acquis par un nombre aleatoire selon le nombre element de la liste %char%
            digit = random.randint(0, len(self.char)) - 1

            # concatenation du caratere issu du random à son index %digit% recu aleatoirement
            ## print(digit,">",self.char[digit])
            code += self.char[digit]

        print(code)

# appel de la classe
for i in range (100) :
    MotDePasse()

## for cpt in range(0,100) :
    ## MotDePasse()