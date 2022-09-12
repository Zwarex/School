from images import *

### MAIN ###

def seuil(data: list)->int :
    moyenne = 0 
    for x in range(len(data[0])):
        for px in range(len(data)): 
            moyenne += data[x][px]

    return moyenne//(len(data[0])*len(data))

def noir_blanc(data: list)->list:
	seuil_moyen = seuil(data)
	for x in range(len(data[0])):
		for i in range(len(data)):
			if data[x][i] >= seuil_moyen :
				data[x][i] = 255
			else :
				data[x][i] = 0
	return data
				
				


## input ##

images = input("Nom de l'image : ")
tableau = get_data_from_image(images)
noir_blanc(tableau)

"""
print(tableau[0])
print(tableau[7][2]) #value 8,3
print(len(tableau)) #lignes
print(len(tableau[1])) #colones
"""
