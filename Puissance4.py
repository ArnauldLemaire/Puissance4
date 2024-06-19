import numpy as np
import random as rd

ROUGE = "\033[0;31m"
BLEU =  "\033[0;34m"
RAZCOULEUR = "\033[0m"

# On creer une grille de dimension 6 x 7 remplie de 0
def grilleVide() :
    return np.zeros((6,7))

# On defini l'affichage de la grille
def afficheGrille(grille) :
    print(" 0 1 2 3 4 5 6")
    print("---------------")
    for i in range(6):
        s = ""
        s +="|"
        for j in range(7) :
            t = grille[i,j]
            if t == 0 :
                s += "."
            elif t == 1 :
                s += ROUGE + "X" + RAZCOULEUR
            else :
                s += BLEU + "O" + RAZCOULEUR
            s += "|"
        print(s)

# On test si le coup est possible
def coupPossible(grille, colonne) :
    if (0 <= colonne) & (colonne <7) :
        i = 5
        test = (grille[i,colonne] != 0)
        while (i>0) & (test):
            test = (grille[i-1,colonne] != 0)
            i -= 1
        return not test
    else :
        return False

# On joue dans la grille
def jouer(grille, joueur, colonne) :
    i = 5
    t = grille[i,colonne]
    while ((t != 0) & (i>0)) :
        i -= 1
        t = grille[i,colonne]
    grille[i,colonne] = joueur
    return grille

# On test les combinaisons gagnantes
def ligneVersDroite(grille, joueur, ligne, colonne) :
    t = grille[ligne,colonne]
    if t == joueur :
        compteur = 1
        for i in range (1,4):
            if (colonne+i < 7) :
                if (grille[ligne,colonne+i] == t):
                    compteur += 1
        return (compteur == 4)
    else :
        return False

def ligneVersBas(grille, joueur, ligne, colonne) :
    t = grille[ligne,colonne]
    if t == joueur :
        compteur = 1
        for i in range(1,4):
            print
            if (ligne+i<6) :
                if (grille[ligne+i,colonne] == t) :
                    compteur += 1
        return (compteur == 4)
    else :
        return False

def ligneDiagonaleDroite(grille, joueur, ligne, colonne):
    t = grille[ligne,colonne]
    if t == joueur :
        compteur = 1
        for i in range(1,4):
            if (colonne+i < 7) & (ligne+i < 6) :
                if (grille[ligne+i,colonne+i] == t):
                    compteur += 1
        return  (compteur == 4)
    else :
        return False

def ligneDiagonaleGauche(grille, joueur, ligne, colonne):
    t = grille[ligne,colonne]
    if t == joueur :
        compteur = 1
        for i in range(1,4):
            if (colonne-i >=0) & (ligne+i < 6) :
                if (grille[ligne+i,colonne-i] == t):
                    compteur += 1
        return  (compteur == 4)
    else :
        return False

# On test si un joueur a gagne la partie
def gagne(grille, joueur) :
    test = False
    i = 0
    while (i<6) & (not test) :
        j = 0
        while (j<7) & (not test):
            test = ligneVersDroite(grille,joueur,i,j) | ligneVersBas(grille,joueur,i,j) | ligneDiagonaleGauche(grille,joueur,i,j) | ligneDiagonaleDroite(grille,joueur,i,j)
            j += 1
        i += 1
    return test

# On test si la partie est finie
# Soit parce que quelqu'un a gagne soit parce que la grille est remplie
def partieFinie(grille):
    test = True
    i = 0
    while (i<6) & test :
        j = 0
        while (j<7) & test :
            test = (grille[i,j]!=0)
            j += 1
        i += 1
    return test | gagne(grille,1) | gagne(grille,2)

# vide la ligne de la gille
def videLigne(ligne):
    for i in range(6):
        grille[ligne,i]=0

# Jouons une partie
# Initialisation de la partie
grille = grilleVide()

# On tire au sort le joueur qui commence
joueur = rd.randint(1,2)
# On joue tant que la partie n'est pas finie
while (not partieFinie(grille)) :
    print("C'est au tour du joueur ", joueur, " de jouer !")
    afficheGrille(grille)
    colonne = int(input("Dans quelle colonne voulez-vous jouez ?"))
    # On test si le coup est possible
    while (not coupPossible(grille, colonne)) :
        print("Impossible de jouer dans cette colonne")
        afficheGrille(grille)
        colonne = int(input("Dans quelle colonne voulez-vous jouez ?"))
    # On joue
    jouer(grille,joueur, colonne)
    # On test si le joueur a gagné
    if (not gagne(grille, joueur)) :
        if joueur == 1 :
            joueur = 2
        else :
            joueur = 1

afficheGrille(grille)
# On test pour quelle raison la partie s'est finie
if gagne(grille, joueur) :
    print("Félicitation !! Le joueur ", joueur, "a gagné !!!")
else :
    print("Le jeu est fini. La grille est pleine !! ")