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

            if action.key == pygame.K_d:
                self.deplacement.x = self.vitesse
                self.updtateSprite('walk')
                self.gauche = False
            elif action.key == pygame.K_q:
                self.deplacement.x = -self.vitesse
                self.updtateSprite('walkGauche')
                self.gauche = True
            elif action.key == pygame.K_SPACE:
                if self.gauche:
                    self.updtateSprite('jumpGauche')
                    # self.deplacement.x = -self.vitesse
                    # self.deplacement.y = -2
                else:
                    self.updtateSprite('dead')
                    # self.deplacement.x = self.vitesse
                    # self.deplacement.y = -2



        elif action.type == pygame.KEYUP:

            self.deplacement = pygame.math.Vector2(0, 0)

            if action.key == pygame.K_d or action.key == pygame.K_q:
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

    def update(self, dt, screen):
        self.sprite.deplacement = self.deplacement
        self.group.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).
        self.group.draw(self.fenetre)


    def move(self,camera_pos):
        pos_x,pos_y = camera_pos # Split camara_pos
        #
        key = pygame.key.get_pressed() # Get Keyboard Input
        if key[pygame.K_z]: # Check Key
            self.sprite.rect.y -= 8 # Move Player Rect Coord
            pos_y += 8 # Move Camara Coord Against Player Rect
        if key[pygame.K_q]:
            self.sprite.rect.x -= 8
            pos_x += 8
        if key[pygame.K_s]:
            self.sprite.rect.y += 8
            pos_y -= 8
        if key[pygame.K_d]:
            self.sprite.rect.x += 8
            pos_x -= 8
        #
        if self.sprite.rect.x < 0: # Simple Sides Collision
            self.sprite.rect.x = 0 # Reset Player Rect Coord
            pos_x = camera_pos[0] #Reset Camera Pos Coord
        elif self.sprite.rect.x > 984:
            self.sprite.rect.x = 984
            pos_x = camera_pos[0]
        if self.sprite.rect.y < 0:
            self.sprite.rect.y = 0
            pos_y = camera_pos[1]
        elif self.sprite.rect.y > 984:
            self.sprite.rect.y = 984
            pos_y = camera_pos[1]
        #
        return (pos_x,pos_y) # Return New Camera Pos