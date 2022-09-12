from PIL import Image

def get_data_from_image(nom: str)->list:
    '''
        Ouvre un fichier image et renvoie la matrice des valeurs des pixels la constituant.

        ENTREE : nom = le nom du fichier image
        SORTIE : la matrice des valeurs de pixels
    '''
    photo = Image.open(nom)
    pixels = photo.load()
    data = []
    width, height = photo.size
    for y in range(height):
        ligne = []
        for x in range(width):
            ligne.append(pixels[x, y])
        data.append(ligne)
    return data

def save_image_from_data(nom: str, data: list)->None:
    '''
        Enregistre un fichier image à partir de la matrice des valeurs des pixels la constituant.
        FORMAT NIVEAUX DE GRIS ( pixels codés sur un seul entier à 8 bits, 0 = noir -> 255 = blanc )
        ENTREES :   nom =  le nom du fichier image
                    data = la matrice des valeurs de pixels
        SORTIE : aucune
    '''
    h = len(data)
    l = len(data[0])
    photo = Image.new('L',(l, h))
    pixels = photo.load()
    for y in range(h):
        for x in range(l):
            pixels[x, y] = data[y][x]
    photo.save(nom)


