from math import sqrt
import csv
from traceback import print_tb
import matplotlib.pyplot as plt

""""
parametres 
"""

long1 = float(input("une valeur : "))
larg1 = float(input("une valeur : "))
tab_distance = []
mini =0
couleur_iris = 0
longueur_iris,largeur_iris,espece = [],[],[]

""" 
fonctions 
"""

def lecture_fichier(file,longueur,largeur,espece):
    """
    fonction qui lit et ecrit le contenu du fichier 
    et qui renvoie la largeur longueur et l'espece dans des tableaux différents 
    """
    fichier = open(file, 'r')
    tableau = csv.reader(fichier, delimiter=",")
    for colonnes in tableau : 
        if colonnes[0][0] != '#':
            longueur.append(float(colonnes[0]))
            largeur.append(float(colonnes[1]))
            espece.append(float(colonnes[2]))
    return longueur_iris, largeur_iris, espece 


def affichage_graphique(x,y,espece):  #x = longueur, y = largeur 
    """
    fonction qui affiche le graphique sans le kkpv
    """
    for longueur,largeur,plante in zip(x,y,espece):
        if plante == 0 :
            plt.plot(longueur,largeur,"+b") 
        elif plante == 1 : 
            plt.plot(longueur,largeur, "+r")
        else :
            plt.plot(longueur,largeur, "+g")
    plt.show()
    return

def distance_kppv(x1,y1,x2,y2):
    """
    cette fonction calcule toutes les distances pour les mettre dans un tableau et sortir sa plus petite valeur
    """
    for t,i in zip(x2,y2) : 
        dist = sqrt((t-x1)**2+(i-y1)**2)
        tab_distance.append(dist)
    print(tab_distance)
    mini = min(tab_distance)
    print(mini)
    return mini,tab_distance


def kppv(mini,tab_distance):
    """
    cette fonction trouve le kppv
    """
    compteur = 0
    tab = 0
    while tab != mini : 
        tab = tab_distance[compteur]
        compteur += 1
    if compteur <= 50 : #nombre ou d'iris de couleur 0
        couleur_iris = 0
    elif compteur >= 51 and compteur <= 101: #nombre d'iris de couleur 1
        couleur_iris = 1
    else :
        couleur_iris = 2
    return couleur_iris

""" 
lancement des fonctions 
"""

lecture_fichier("iris.csv",longueur_iris,largeur_iris,espece)
#affichage_graphique(longueur_iris,largeur_iris,espece)
distance_kppv(long1,larg1,longueur_iris,largeur_iris)
kppv(mini,tab_distance)

if couleur_iris == 0 : 
    print("l'iris est une setosa")
elif couleur_iris == 1 :
    print("l'iris est une verginica")
else : 
    print("l'iris est une versicolor")