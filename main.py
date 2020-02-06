import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from ennemy import *
from game import Game
from  maps import *
from sprite import Sprite
import pygame.freetype
from  changementSalles import *
from tkinter import *

pygame.font.init()
pygame.init()

white = pygame.color.Color('#ffffff')
red = pygame.color.Color('#ff0000')
black = pygame.color.Color('#000000')
clock = pygame.time.Clock()
font = pygame.font.Font('Font/Pixeled.ttf', 20)
# font_content = pygame.font.Font(None, 30)
font_content = pygame.font.Font('Font/FreePixel.ttf', 18)

text = font.render('A BOUT DE SOUFFLE', True, white)
text_play = font.render('Jouer', True, white)
text_instructions = font.render('Commandes', True, white)
text_credits = font.render('Credits', True, white)
text_back = font.render('Retour', True, white)

bg = pygame.image.load("Assets/Background/main_bg.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
babel = pygame.image.load("Assets/Background/babel.png")

# tour = Sprite('Assets/Background/background_accueil.png', 1, 1, colorkey=False)
# tour = pygame.image.load('Assets/Background/background_accueil.png')
# perso_assie = Sprite('Assets/Player/perso_assi.png', 10, 1, scale=4)

marge = 40
button_width = 240
button_height = 80

# Menu principal
def start_menu(screen):

    if not pygame.mixer.get_busy():
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("Audio/2.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    start = True
    while start:
        clock.tick(70)
        #2.56
        # tour.draw(screen, 0, 0 )
        # screen.blit(tour, (0, 0))
        screen.blit(babel, ((0.5*WIDTH)-(0.5*babel.get_width()),(0.5*HEIGHT)-(0.5*babel.get_height())))
        # tour.draw(screen, 0, 0)
        # perso_assie.draw(screen, 100, 100)

        action = None
        pos = pygame.mouse.get_pos()
        colour = red

        bt = Sprite('Assets/boutons/button.png', 1, 1, scale=4, colorkey=0)
        bt.draw(screen, WIDTH / 2 - button_width / 2, HEIGHT / 2 + 30, handle=0)


        if pos[0] >= WIDTH/2 - button_width/2 and pos[0] <= WIDTH/2 + button_width/2 and pos[1] >= HEIGHT/2 + 30 and pos[1] <= HEIGHT/2 + 30 + button_height:
            colour = white
            action = "start"
            bt.draw(screen, WIDTH / 2 - button_width / 2, HEIGHT / 2 + 30, handle=0)

        bt.draw(screen, WIDTH - (button_width + marge), HEIGHT - (button_height + marge), handle=0)

        colour = red
        if pos[0] >= WIDTH - (button_width + marge) and pos[0] <= WIDTH - marge and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "credits"
            bt.draw(screen, WIDTH - (button_width + marge), HEIGHT - (button_height + marge), handle=0)

        # pygame.draw.rect(screen, colour, (WIDTH - (button_width + marge), HEIGHT - (button_height + marge), button_width, button_height))

        bt.draw(screen, marge, HEIGHT - (button_height + marge), button_width, handle=0)

        colour = red
        if pos[0] >= marge and pos[0] <= marge + button_width and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "instructions"
            bt.draw(screen, marge, HEIGHT - (button_height + marge), button_width, handle=0)

        # pygame.draw.rect(screen, colour, (marge, HEIGHT - (button_height + marge), button_width, button_height))

        screen.blit(text, (WIDTH/2 - text.get_rect().width/2, 100))
        screen.blit(text_play, (WIDTH / 2 - text_play.get_rect().width / 2, HEIGHT/2 + 36))
        screen.blit(text_instructions, (marge + 30, HEIGHT - (marge + 75)))
        screen.blit(text_credits, (WIDTH - (marge + (button_width - 50)), HEIGHT - (marge + 75)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action is not None:
                    return action

def display_credits(screen):

    text_credits_content = font.render('CREDITS :', True, white)

    text_credits_ideos = font_content.render('Jeu développé par l\'équipe IDEOS', True, white)


    text_credits_game_design = font_content.render('Game Design : Mike le Québecois', True, white)
    text_credits_developpers = font_content.render('Développement : HERVE David, GODEFROID Louis, PEYRIN Florent', True, white)
    text_credits_level_design = font_content.render('Level Design : GODEFROID Louis', True, white)
    text_credits_design = font_content.render('Graphisme : VIALLON Gabriel', True, white)
    text_credits_sound_design = font_content.render('Sound Design : PEYRIN Florent', True, white)

    text_credits_sound_original = font_content.render('Bande son originale composée par PEYRIN Florent', True, white)
    text_credits_graphism_original = font_content.render('Dessins originaux et animations élaborés par VIALLON Gabriel', True, white)

    while True:
        action = None
        pos = pygame.mouse.get_pos()
        screen.fill(black)

        bt = Sprite('Assets/boutons/button.png', 1, 1, scale=4, colorkey=0)
        bt.draw(screen, WIDTH - (button_width + marge), HEIGHT - (button_height + marge), handle=0)

        colour = red
        if pos[0] >= WIDTH - (button_width + marge) and pos[0] <= WIDTH - marge and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "back"
            bt.draw(screen, WIDTH - (button_width + marge), HEIGHT - (button_height + marge), handle=0)

        # pygame.draw.rect(screen, colour, (WIDTH - (button_width + marge), HEIGHT - (button_height + marge), button_width, button_height))

        screen.blit(text_credits_content, (marge, marge))
        screen.blit(text_credits_ideos, (marge, marge + 90))
        screen.blit(text_credits_game_design, (marge, marge + 140))
        screen.blit(text_credits_developpers, (marge, marge + 190))
        screen.blit(text_credits_level_design, (marge, marge + 240))
        screen.blit(text_credits_design, (marge, marge + 290))
        screen.blit(text_credits_sound_design, (marge, marge + 340))

        screen.blit(text_credits_sound_original, (marge, marge + 390))
        screen.blit(text_credits_graphism_original, (marge, marge + 440))

        screen.blit(text_back, (WIDTH - (marge + (button_width - 60)),HEIGHT - (marge + 75)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action is not None:
                    return action


def display_instructions(screen):

    text_instructions_content = font.render('COMMANDES :', True, white)

    text_instructions_resume = font_content.render('Après avoir reçu la bénédiction d\'Eole, le flûtiste Alexios fût contraint de gravir au sommet de la ', True, white)
    text_instructions_resume2 = font_content.render('Tour des Dieux afin de prouver sa bravoure.', True, white)
    text_instructions_resume3 = font_content.render('Accompagné de son instrument enchanté, il devra braver les plus grands dangers ', True, white)
    text_instructions_resume4 = font_content.render('et atteindre le sommet sans recourir aux armes ou à la violence...', True, white)

    text_instructions_move = font_content.render('Utilisez Z, Q, S, D pour vous déplacer et les flèches directionnelles pour contrôler le vent.', True, white)
    text_instructions_ennemy = font_content.render('Durant son périple, Alexios croisera le chemin de divers ennemis avec leurs particularités :', True, white)

    text_instructions_minotaur1 = font_content.render('LE MINOTAURE :', True, white)

    text_instructions_minotaur2 = font_content.render('Ce monstre de chair vous réduira en', True, white)
    text_instructions_minotaur3 = font_content.render('miettes si vous entrez dans sa lumière.', True, white)
    text_instructions_minotaur4 = font_content.render('Utilisez votre flûte pour éteindre sa', True, white)
    text_instructions_minotaur5 = font_content.render('torche et ainsi le rendre inoffensif', True, white)
    text_instructions_minotaur6 = font_content.render('pendant quelques secondes.', True, white)

    img_minotaur = pygame.image.load("Assets/Minotaur/mino_normal.png")
    img_minotaur_scale = pygame.transform.rotozoom(img_minotaur, 0, 2)

    text_instructions_siren = font_content.render('LA SIRENE :', True, white)

    text_instructions_siren1 = font_content.render('Elle vous attendra sur son rocher en', True, white)
    text_instructions_siren2 = font_content.render('chantant afin de vous attirer.', True, white)
    text_instructions_siren3 = font_content.render('Restez en dehors de sa portée pour', True, white)
    text_instructions_siren4 = font_content.render('rester en vie !', True, white)

    img_siren = pygame.image.load("Assets/Siren/sirene_normale.png")

    while True:
        action = None
        pos = pygame.mouse.get_pos()
        screen.fill(black)

        colour = red
        bt = Sprite('Assets/boutons/button.png', 1, 1, scale=4, colorkey=0)
        bt.draw(screen, WIDTH - (button_width + marge), HEIGHT - (button_height + marge), handle=0)

        if pos[0] >= WIDTH - (button_width + marge) and pos[0] <= WIDTH - marge and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "back"
            bt.draw(screen, WIDTH - (button_width + marge), HEIGHT - (button_height + marge), handle=0)

        # pygame.draw.rect(screen, colour, (WIDTH - (button_width + marge), HEIGHT - (button_height + marge), button_width, button_height))

        screen.blit(text_instructions_content, (marge, marge))
        screen.blit(text_instructions_resume, (marge, marge + 80))
        screen.blit(text_instructions_resume2, (marge, marge + 110))
        screen.blit(text_instructions_resume3, (marge, marge + 140))
        screen.blit(text_instructions_resume4, (marge, marge + 170))

        screen.blit(text_instructions_move, (marge, marge + 230))

        screen.blit(text_instructions_ennemy, (marge, marge + 290))

        screen.blit(text_instructions_minotaur1, (marge, marge + 350))
        screen.blit(img_minotaur_scale, (marge, 430))
        screen.blit(text_instructions_minotaur2,(marge, 520))
        screen.blit(text_instructions_minotaur3,(marge, 550))
        screen.blit(text_instructions_minotaur4,(marge, 580))
        screen.blit(text_instructions_minotaur5,(marge, 610))
        screen.blit(text_instructions_minotaur6,(marge, 640))

        screen.blit(text_instructions_siren, (marge + 500, marge + 350))
        screen.blit(img_siren, (marge + 500, 430))
        screen.blit(text_instructions_siren1, (marge + 500, marge + 475))
        screen.blit(text_instructions_siren2, (marge + 500, marge + 505))
        screen.blit(text_instructions_siren3, (marge + 500, marge + 535))
        screen.blit(text_instructions_siren4, (marge + 500, marge + 565))

        screen.blit(text_back, (WIDTH - (marge + (button_width - 60)),HEIGHT - (marge + 75)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action is not None:
                    return action

def main(screen: pygame.display) -> None:

    #--------------------------------------------------------------------------------
    salles = {
        1: Game(map=etage1, fond=fond1, objets=(), player=Player(0, 0), enemies=enemies1),
        2: Game(map=etage2, fond=fond2, objets=(), player=Player(0, 0), enemies=enemies2),
        3: Game(map=etage3, fond=fond3, objets=(), player=Player(0, 0), enemies=enemies3),
        4: Game(map=etage4, fond=fond4, objets=(), player=Player(0, 0), enemies=enemies4),
        5: Game(map=etage5, fond=fond5, objets=(), player=Player(0, 0), enemies=enemies5),
        6: Game(map=etage6, fond=fond6, objets=(), player=Player(0, 0), enemies=enemies6),
        7: Game(map=etage7, fond=fond7, objets=(), player=Player(0, 0), enemies=enemies7),
        8: Game(map=etage8, fond=fond8, objets=(), player=Player(0, 0), enemies=enemies8),
        9: Game(map=etage9, fond=fond9, objets=(), player=Player(0, 0), enemies=enemies9)

    }
    index = 1
    game = salles[index]
    #--------------------------------------------------------------------------------
    clock = pygame.time.Clock()

    #Sound
    game.initMixer()
    sound_channel_player = pygame.mixer.Channel(0)
    sound_channel_ennemy = pygame.mixer.Channel(1)
    sound_channel_ambient = pygame.mixer.Channel(2)

    channels = []
    channels.append(sound_channel_player)
    channels.append(sound_channel_ennemy)
    channels.append(sound_channel_ambient)

    sound_player_jump = pygame.mixer.Sound("Audio/Fx/jump1.ogg")

    sound_flute = pygame.mixer.Sound("Audio/Fx/flute.ogg")
    sound_step = pygame.mixer.Sound("Audio/Fx/step.ogg")

    sound_minotaur1 = pygame.mixer.Sound("Audio/Fx/minotaur1.wav")
    sound_minotaur2 = pygame.mixer.Sound("Audio/Fx/minotaur2.wav")

    sounds_minotaur = []
    sounds_minotaur.append(sound_minotaur1)
    sounds_minotaur.append(sound_minotaur2)

    sound_blow = pygame.mixer.Sound("Audio/Fx/blow.wav")

    sounds_ambient = []
    sounds_ambient.append(sound_blow)
    running = TRUE
    while running:
        events()
        #------------------------------------------
        if game.display(screen):
            index += 1
            if index > len(salles):
                print("fin du jeu")
                return None
            else:
              game = salles[index]

        #------------------------------------------
        game.playMixerEnnemy(channels[1], sounds_minotaur)
        game.playMixerPlayer(channels[0], sound_player_jump, sound_flute, sound_step)
        game.playMixerAmbiant(channels[2], sound_blow)
        pygame.display.update()
        screen.fill((35, 118, 211))
        
        clock.tick(FPS)

if __name__ == '__main__':

    screen = init()
    menu = True
    while RUNNING:
        if menu:
            ans = start_menu(screen)
            if ans == "start":
                # menu = False
                main(screen)
            elif ans == "credits":
                menu = False
                ans2 = display_credits(screen)
                if ans2 == "back":
                    menu = True
            elif ans == "instructions":
                menu = False
                ans3 = display_instructions(screen)
                if ans3 == "back":
                    menu = True

