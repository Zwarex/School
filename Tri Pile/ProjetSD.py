### IMPORT ###
""" Utilisation d'une Pile Dynamique """
from PileDynamique import *
from random import randint

### START ###
""" Ne pas modifier """

def creerPile():
    """
	création de pile vide
	Input : None
	Output : Pile vide
    """
    Pile = PileDynamique()
    return Pile

def remplissagePile(Pile):
    """
	remplissage aléatoire de la pile
	Input : Pile
	Output : Pile remplie aléatoirement
    """
    for i in range(10):
        Pile.empiler(randint(0,9))
    return Pile

### MAIN ### 
""" Main ne pas modifier """

def triPile(Pile):
    """
	Tri de Pile
	Input : Pile
	Output : Pile triée
    """
    if Pile.get_len() == 0 : #Pile vide
        return "Y'a anguille sous roche"
    
    if Pile.get_value(1) != Pile.get_min_value() : #Pile qui ne peut pas être triée
        return "Y'a aussi anguille sous rouche"
    
    Pile_temp = PileDynamique()
    past_elmnt, elmnt = Pile.get_value(0), Pile.get_value(1)
    Pile_temp.empiler(Pile.depile_first())

    for i in range(Pile.get_len()) :
        elmnt = Pile.get_value(0)
        if past_elmnt > elmnt :
            Pile_temp.empiler(elmnt)
        elif Pile_temp.get_min_value() < elmnt : #Si valeur min de la pile plus petite que la valeur actuelle
            while Pile_temp.get_min_value() <= elmnt : #empiler sur pile la valeur depiler sur Pile_temp
                Pile.empiler(Pile_temp.depiler()) #jusqu'à la valeur plus grande ou la fin de la pile_temp
            Pile_temp.empiler(elmnt)
        else :
            Pile_temp.empiler(elmnt)
        past_elmnt = Pile.get_value(0)
        Pile.depile_first()
    for i in range(Pile_temp.get_len()):
        Pile.empiler(Pile_temp.depiler())
    return Pile.get_pile()

### INPUT ###
""" Peut être modifié """

''' Test de base - Fonctionel '''
# Pile = PileDynamique()
# Pile.empiler(4)
# Pile.empiler(1)
# Pile.empiler(3)
# Pile.empiler(2)
# print(triPile(Pile))

''' Test sur Pile random de 10 éléments - Pile non triable gérée - Non fonctionel '''
# print(triPile(remplissagePile(creerPile())))

''' Test Pile du site '''
# Pile = PileDynamique()
# Pile.empiler_tab([3,1,2,5,4]) #Pile triable
# print(triPile(Pile))

# Pile = PileDynamique()
# Pile.empiler_tab([2,4,1,3]) #Pile non triable
# print(triPile(Pile))

# Pile = PileDynamique()
# Pile.empiler_tab([4,5,3,7,2,1,6]) #Pile non triable
# print(triPile(Pile))
