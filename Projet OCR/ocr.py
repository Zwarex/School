from images import *

### MAIN ###

def seuil(tab: list)->int :
    moyenne = 0 
    for x in range(len(tab[0])):
        for px in range(len(tab)): 
            moyenne += tab[x][px]

    return moyenne//(len(tab[0])*len(tab))

def noir_blanc(data: list)->list:
	seuil_moyen = seuil(data)
	for x in range(len(data[0])):
		for i in range(len(data)):
			if data[x][i] >= seuil_moyen :
				data[x][i] = 255
			else :
				data[x][i] = 0
	return data
				
def traitement(data1: list, data2: list)->list:
	tab1 = noir_blanc(data1)
	tab2 = noir_blanc(data2)
	tab_xor = tab1.copy()
	tab_and = tab1.copy()
	
	for i in range(len(tab1)) :
		for px in range(len(tab1[i])) :
			tab_xor[i][px] = tab1[i][px] ^ tab2[i][px]
			tab_and[i][px] = tab_xor[i][px] & tab2[i][px]	
		return tab_xor

def ocr(nom: str)->str:
	liste = [chr(i) for i in range(65,91)]
	dic = {}
	for i in liste :
		px_blanc = 0
		nom2 = liste[i]
		tab_caract = traitement(nom,nom2)
		for i in range(len(tab_caract[0])) : 
			for y in range(len(tab_caract)) :
				if tab_caract[i][y] == 255 :
					px_blanc += 1
		dic[liste[i]] = px_blanc
	print(dic)
	return
		

## input ##

image_ = input("Votre fichier : ")
image1 = get_data_from_image(image_)
ocr(image1)
"""
print(tableau[0])
print(tableau[7][2]) #value 8,3
print(len(tableau)) #lignes
print(len(tableau[1])) #colones
"""
