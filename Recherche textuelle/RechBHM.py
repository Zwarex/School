


def decalages(motif: str)->dict:
    '''
    Fonction qui calcule le décalage pour chaque caractère d'un motif.
    Entrée :
    motif = le motif à pré-traite
    Sortie :
    le dictionnaire associant à chaque caractère ( clé ) son décalage ( valeur )
    '''
    dic = {}
    for i in range(len(motif)):
        dic[motif[i]] = len(motif)-i-1
    return dic

	

def rechBHM(texte,motif):
    occurences = []
    dec = decalages(motif)
    n = len(texte)
    p= len(motif)
    
    i=0
    while i <= n-p :
        j = p -1
        while j >= 0 and texte[i+j] == motif[j] :
            j -= 1

        if j == - 1 :
            occurences.append(i)
            i += p
        elif texte[i+j] == motif[p-1]:
            i += p
        elif texte[i+j] not in motif :
            i += p
        else :
            i += dec[texte[i+j]]
    if len(occurences) == 0 :
        return False
    else :
        return occurences

print(rechBHM("Un chasseur sachant chasser doit savoir chasser sans son chien","ch"))