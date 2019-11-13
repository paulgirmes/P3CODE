"""
Mac Gyver maze Game, help Mc Gyver to escape the maze, move with arrows, 
collect each item before reaching the guarded exit to win the game.

Python Script
Files : MacGyverMaze.py, classes.py, constants.py, level1.json + images
"""
import pygame
from pygame.locals import *
import classes as cl
import constants as ct
""" 
pygame.init()

fenetre = pygame.display.set_mode((ct.cote_fenetre, ct.cote_fenetre))
icone  = pygame.image.load(ct.image_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(ct.titre_fenetre)


while True:
    pass
 """

""" 
BOUCLE PRINCIPALE:
     BOUCLE DE MENU:
          #Limitation de vitesse de la boucle
#30 frames par secondes suffisent
pygame.time.Clock().tick(30)

          fin de la boucle de menu

     BOUCLE DE JEU:
     #Limitation de vitesse de la boucle
#30 frames par secondes suffisent
pygame.time.Clock().tick(30)

          fin de la boucle de jeu """

gyver = cl.Character()
print(gyver)
print(gyver.sprite_location)

