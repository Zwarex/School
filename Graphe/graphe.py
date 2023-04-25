class Graphe:
    
    def __init__(self, S = None):
        '''Méthode qui crée un graphe vide ou à partir d'une liste de sommets.
        Entrée :
            S = la liste des sommets du graphe ( None par défaut )
        '''
        if S != None :
            self.graphe = {i for i in S}
        else :
            self.graphe = {}    

    def ajoute_sommet(self, id: str):
        '''Méthode qui ajoute un unique sommet au graphe.
            Entrée :
                id = l'identifiant du sommet dans le graphe
            Lève une exception au cas où l'identifiant existe déjà dans le graphe
        '''
        assert id not in self.graphe , "Id deja présent"
        self.graphe[id] = []

    def ajoute_arc(self, id1: str, id2: str):
        '''Méthode qui créé un arc entre deux sommets.
        Entrées :
            id1 = identifiant du sommet de départ de l'arc
            id2 = identifiant du sommet de fin de l'arc
        Lève une exception au cas où l'identifiant d'un des sommets n'existe pas dans le graphe
        '''   
        assert id1 in self.graphe and id2 in self.graphe , "Pas d'id1 ou d'id2 dans graphe"
        self.graphe[id1].append(id2)

    def ajoute_arete(self, id1: str, id2: str):
        '''Méthode qui créé une arête entre deux sommets.
        Entrées :
            id1 = identifiant du sommet de départ de l'arc
            id2 = identifiant du sommet de fin de l'arc
        Lève une exception au cas où l'identifiant d'un des sommets n'existe pas dans le graphe
        '''
        assert id1 in self.graphe and id2 in self.graphe , "Pas d'id1 ou d'id2 dans graphe"
        self.graphe[id1].append(id2)
        self.graphe[id2].append(id1)

    
    def adjacents_de(self, id: str)->list:
        '''Méthode qui renvoie la liste des sommets adjacents (voisins ou successeurs ) d'un sommet donné.
        Entrée :
            id = l'identifiant du sommet
        Sortie :
            la liste des sommets adjacents du sommet passé en paramètre
        Lève une exception si le sommet n'existe pas dans le graphe.
        '''
        assert id in self.graphe , "Pas de id dans graphe"
        adj = []
        for i in self.graphe[id] :
            adj.append(i)
        return adj

    