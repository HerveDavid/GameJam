# Chargement des modules
try:
    import pygame
    from sprite import Sprite
    from outils import *
except ImportError as err:
    print("Echec importation: {0}").format(err)

# Classe pour la création du joueur
class Player():

    def __init__(self, nomJoueur: str, fenetre, fichierAssert='assert/player'):


        # Appel du constructeur
        super(Player, self).__init__()

        # Nom du joueur
        self.nom = nomJoueur

        # Fenetre affilié
        self.fenetre = fenetre

        # Déplacement du joueur
        self.deplacement = pygame.math.Vector2(0, 0)

        # Vitesse du joueur
        self.vitesse = 3

        # Vue a gauche
        self.gauche = False

        # Vue en bas
        self.bas = False

        # Chargement des images dans le player avec un dictionnaire
        self.images = chargesImagesDict(fichierAssert)

        # Chargement des images gauches du player
        gauches = ['dead', 'idle', 'jump', 'run', 'walk']
        for i in gauches:
            self.images[str(i + 'Gauche')] = [pygame.transform.flip(image, True, False) for image in self.images[i]]

        # Sprite
        self.sprite = Sprite(self.images['idle'])

        # Group
        self.group  = pygame.sprite.Group(self.sprite)


    def bouger(self, action: pygame.event):

        if action.type == pygame.KEYDOWN:

            if action.key == pygame.K_RIGHT:
                self.deplacement.x = self.vitesse
                self.updtateSprite('walk')
                self.gauche = False
            elif action.key == pygame.K_LEFT:
                self.deplacement.x = -self.vitesse
                self.updtateSprite('walkGauche')
                self.gauche = True
            elif action.key == pygame.K_SPACE:
                if self.gauche:
                    self.updtateSprite('jumpGauche')
                    # self.deplacement.x = -self.vitesse
                    # self.deplacement.y = -2
                else:
                    self.updtateSprite('jump')
                    # self.deplacement.x = self.vitesse
                    # self.deplacement.y = -2



        elif action.type == pygame.KEYUP:

            self.deplacement = pygame.math.Vector2(0, 0)

            if action.key == pygame.K_RIGHT or action.key == pygame.K_LEFT:
                if self.gauche:
                    self.updtateSprite('idleGauche')
                else:
                    self.updtateSprite('idle')

            elif action.key == pygame.K_SPACE:
                if self.gauche:
                    self.updtateSprite('idleGauche')
                    # self.sprite.rect.x = self.sprite.rect.x - self.vitesse
                else:
                    self.updtateSprite('idle')
                #     self.sprite.rect.x = self.sprite.rect.x + self.vitesse
                # self.sprite.rect.y = self.sprite.rect.y - 2

    def updtateSprite(self, dossier: str):
        bufferSprite = self.sprite
        self.sprite = Sprite(self.images[dossier])
        self.sprite.rect = bufferSprite.rect
        self.group.empty()
        self.group.add(self.sprite)

    def update(self, dt):
        self.sprite.deplacement = self.deplacement
        self.group.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).
        self.group.draw(self.fenetre)



