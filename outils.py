# Chargement des modules
try:
    import pygame
    import os
except ImportError as err:
    print(err)

# Constantes
SIZE = WIDTH, HEIGHT = 1024, 768
FPS = 60
VERSION = '0.1'


# charge les images depuis un dossier dans une liste
def chargeImages(dossier: str):
    images = []
    for fichier in os.listdir(dossier):
        image = pygame.image.load(dossier + os.sep + fichier).convert()
        images.append(image)
    return images

# charge les images dans un dictionnaire
def chargesImagesDict(dossier: str):
    dict = {}
    for fichiers in os.listdir(dossier):
        dict[str(fichiers)] = chargeImages(dossier + os.sep +fichiers)
    return dict

