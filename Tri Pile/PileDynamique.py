class PileDynamique:
    def __init__(self):
        self.tab = []

    def est_vide(self):
        return self.tab == []

    def get_pile(self):
        return self.tab

    def empiler(self,donnee):
        self.tab.append(donnee)

    def depiler(self):
        if self.est_vide() == True :
            return "Pile Vide!"
        return self.tab.pop()
    
    def depile_first(self):
        if self.est_vide() == True :
            return "Pile Vide!"
        return self.tab.pop(0)

    def get_len(self):
        return len(self.tab)

    def get_value(self,n):
        return self.tab[n]
    
    def get_min_value(self):
        if self.est_vide() == True :
            return 9999999999999999999999999
        return min(self.tab)

    def empiler_tab(self,tab):
        for i in tab:
            self.tab.append(i)