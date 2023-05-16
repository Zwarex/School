

def recherche_naif(text,motif):
    occurences = []

    for char in range(0,len(text)-len(motif)) :
        j=0
        while j < len(motif) and motif[j] == text[char+j] :
            j += 1 
        if j == len(motif) :
            occurences.append(char)
    if len(occurences) == 0 :
        return False
    return occurences


print(recherche_naif("Un chasseur sachant chasser doit savoir chasser sans son chien","kzeiof"))