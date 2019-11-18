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


pygame.init()


#Limitation de vitesse de la boucle 30 frames par secondes suffisent
pygame.time.Clock().tick(30)

#BOUCLE PRINCIPALE:
# BOUCLE DE MENU:
def menu():
     #menu_window = pygame.display.set_mode((ct.window_size(), ct.window_size()))
     level = "niveau1.json"
     return level    
     # fin de la boucle de menu

     # BOUCLE DE JEU:
def main():
     maze= cl.Maze(menu())
     maze.load_level()
     gyver=cl.Character(maze.sprites)
     maze.display_maze(gyver.location)
     i = 1
     while i:
          pygame.time.Clock().tick(30)
          for event in pygame.event.get():
               if event.type == QUIT:
                    i=0
               if event.type == KEYDOWN:
                    switcher={
                         273: "up",
                         274: "down",
                         276: "left",
                         275: "right"
                         }
                    gyver.move(switcher.get(event.key))
                    if maze.sprites[gyver.location] != "" and maze.sprites[gyver.location] != "guard":
                         gyver.item_carried.append(maze.sprites[gyver.location])
                         maze.sprites[gyver.location]=""
                    maze.display_maze(gyver.location)
          if (gyver.location == maze.sprites.index("guard")) and (len(gyver.item_carried) == len(ct.items_to_collect())):
               i=0



if __name__ == "__main__":
     main()

