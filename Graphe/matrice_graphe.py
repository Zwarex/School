from graphe import Graphe

def matrice_vers_graphe(S:list, M:list)->Graphe:
    '''Fonction qui crée un graphe à partir de la liste de ses sommets et de sa matrice d'adjacence
    Entrée :
    S = liste des sommets du graphe
    M = matrice d'adjacence
    Sortie :
    instance de Graphe
    '''
    graphe = Graphe()
    ele1 = 0
    for ele in S :
        graphe.ajoute_sommet(ele)
    for ligne in M :
        ele2 = 0
        for col in ligne :
            if M[ele1][ele2] == 1 :
                graphe.ajoute_arc(S[ele1],S[ele2])
            ele2 += 1
        ele1 += 1
    return graphe

S = ["A","B","C"]
M = [[0,1,0],[1,0,1],[1,1,0]]
graphe1 = matrice_vers_graphe(S,M)
print(graphe1.adjacents_de("A"))
