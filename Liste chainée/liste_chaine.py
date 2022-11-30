class Maillon:

    def __init__(self, valeur, suivant = None): # création d'un maillon qui ne pointe par défaut vers aucun autre
        self.valeur = valeur
        self.suivant = suivant # suivant est de type Maillon !

class Liste:

    def __init__(self, tete = None): # création liste, vide par défaut si aucun maillon n'est fourni en argument
        self.tete = tete # stockage de sa tête. Le paramètre 'tete' est bien entendu de type Maillon !*

    def is_empty(self):
        """
        Verifie si liste est vide
        Input : None
        Output : True or False
        """
        return self.tete == None

    def list_elements(self):
        """
        Retourne les elements présents dans la liste
        Input : None
        Output : Tableau des elements de Liste
        """
        elements = []
        elmnt = self.tete
        while elmnt.suivant != None :
            elements.append(elmnt.valeur)
            elmnt = elmnt.suivant
        elements.append(elmnt.valeur)
        return elements

    def get_element(self,n):
        """
        Retourne l'element de la liste à len(n)
        Input : n 
        Output : element à len(n)
        """
        ele = self.tete
        if self.len()-1<n:
            return "error"
        for i in range(n):
           ele = ele.suivant
        return ele.valeur

    def len(self):
        """
        Retourne la longeur de la liste
        Input : None
        Output : len(Liste)
        """
        elem = self.tete
        len = 1
        while elem.suivant != None :
            len+=1
            elem = elem.suivant
        return len

    def insert_first(self,element):
        """
        Ajoute un element au début de la liste
        Input : element
        Output : Liste + element à self.tete
        """
        new_element = Maillon(element,self.tete)
        self.tete = new_element

    def append(self,element):
        """
        Ajoute un element à la fin de la liste
        Input : element
        Output : Liste + element à len(Liste)
        """
        if self.len() == 1 :
            Liste1.insert_first(element)
            return "valeur ajoutée"
        new_element = Maillon(element,None)
        elmnt = self.tete
        while elmnt.suivant != None :
            elmnt = elmnt.suivant
        elmnt.suivant = new_element

    def insert(self,indice,element):
        """
        Fonction qui ajoute un element à len(indice)
        Input : indice,element
        Output : Liste + elemnt à len(indice)
        """
        new_element = Maillon(element,None)
        elmnt = self.tete
        for i in range(self.len()-1):
            if i == indice-1:
                new_element.suivant = elmnt.suivant 
                elmnt.suivant = new_element
            elmnt = elmnt.suivant
    
    def pop_first(self):
        """
        Fonction qui supprime le premier element de la liste
        Input : None
        Output : Liste sans le premier element
        """
        if self.is_empty is True :
            return 'Liste vide'
        elmnt = self.tete
        self.tete = elmnt.suivant
    
    def pop_last(self):
        """
        Fonction qui supprime le dernier element de la liste
        Input : None
        Output : Liste sans le dernier element
        """
        if self.is_empty is True :
            return 'Liste vide'
        elmnt = self.tete
        for i in range(self.len()-2):
            elmnt = elmnt.suivant
        elmnt.suivant = None
    
    def pop(self,indice):
        """
        Fonction qui supprime l'element à len(indice) de la liste
        Input : indice
        Output : Liste sans element à len(indice)
        """
        if self.is_empty is True :
            return 'Liste vide'
        elmnt = self.tete
        temp_elmnt = self.tete
        cndt = False
        for i in range(self.len()):
            if i+1 != indice and cndt is False:
                elmnt = elmnt.suivant
            elif cndt is True :
                elmnt = elmnt.suivant
                cndt = False
            else :
                temp_elmnt = elmnt
                temp_elmnt = elmnt.suivant
                elmnt.suivant = temp_elmnt.suivant
                cndt = True
        
