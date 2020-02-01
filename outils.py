# Chargement des modules
try:
    import pygame
    import os
except ImportError as err:
    print(err)

# charge les images depuis un dossier dans une liste
def chargeImages(dossier: str):
    images = []
    for fichier in os.listdir(dossier):
        image = pygame.image.load(dossier + os.sep + fichier).convert()
        images.append(image)
    return images