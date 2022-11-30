class Maillon:

    def __init__(self, valeur, suivant = None): # création d'un maillon qui ne pointe par défaut vers aucun autre
        self.valeur = valeur
        self.suivant = suivant # suivant est de type Maillon !

class Liste:

    def __init__(self, tete = None): # création liste, vide par défaut si aucun maillon n'est fourni en argument
        self.tete = tete # stockage de sa tête. Le paramètre 'tete' est bien entendu de type Maillon !*

    def is_empty(self):
        return self.tete == None

    def list_elements(self):
        elements = []
        elmnt = self.tete
        while elmnt.suivant != None :
            elements.append(elmnt.valeur)
            elmnt = elmnt.suivant
        elements.append(elmnt.valeur)
        return elements

    def get_element(self,n):
        ele = self.tete
        if self.len()-1<n:
            return "error"
        for i in range(n):
           ele = ele.suivant
        return ele.valeur

    def len(self):
        elem = self.tete
        len = 1
        while elem.suivant != None :
            len+=1
            elem = elem.suivant
        return len

    def insert_first(self,element):
        new_element = Maillon(element,self.tete)
        self.tete = new_element

    def append(self,element):
        if self.len() == 1 :
            Liste1.insert_first(element)
            return "valeur ajoutée"
        new_element = Maillon(element,None)
        elmnt = self.tete
        while elmnt.suivant != None :
            elmnt = elmnt.suivant
        elmnt.suivant = new_element

    def insert(self,indice,element):
        new_element = Maillon(element,None)
        elmnt = self.tete
        for i in range(self.len()-1):
            if i == indice-1:
                new_element.suivant = elmnt.suivant 
                elmnt.suivant = new_element
            elmnt = elmnt.suivant
    
    def pop_first(self):
        if self.is_empty is True :
            return 'Liste vide'
        elmnt = self.tete
        self.tete = elmnt.suivant
    
    def pop_last(self):
        if self.is_empty is True :
            return 'Liste vide'
        elmnt = self.tete
        for i in range(self.len()-2):
            elmnt = elmnt.suivant
        elmnt.suivant = None
    
    def pop(self,indice):
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
        

            
            

Liste1 = Liste(Maillon(1,Maillon(4,Maillon(7,Maillon(7,Maillon(90,Maillon('aaa',)))))))
print(Liste1.pop(3))
print(Liste1.list_elements())
