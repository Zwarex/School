from graphe import Graphe


def vers_matrice(G: Graphe)->list:
    '''Fonction qui renvoie la matrice d'adjacence du graphe à partir d'une instance de GrapheD.
    Entrée :
    G = objet de type Graphe
    Sorties :
    la liste des sommets, et la matrice d'adjacence
    Lève une exception si le graphe est vide.
    '''
    assert G.graphe is not None, "Graphe Vide"
    sommets = [ele for ele in G.graphe.keys()]
    adjacence = [[0 for i in range(len(sommets))]for i in range(len(sommets))]

    ele1 = 0
    for ligne in adjacence :
        id1 = sommets[ele1]
        liste_adj = G.adjacents_de(id1)
        ele2 = 0
        for col in ligne :
            id2 = sommets[ele2]
            if id2 in liste_adj :
                adjacence[ele1][ele2] = 1
            ele2 +=1    
        ele1 +=1
    return adjacence

graphe = Graphe()
graphe.ajoute_sommet(1)
graphe.ajoute_sommet(2)
graphe.ajoute_sommet(3)
graphe.ajoute_arete(1,2)
graphe.ajoute_arete(1,3)

print(vers_matrice(graphe))