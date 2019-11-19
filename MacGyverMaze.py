"""
Mac Gyver maze Game, help Mc Gyver to escape the maze, move with arrows, 
collect each item before reaching the guarded exit to win the game.

Python Script
Files : MacGyverMaze.py, classes.py, constants.py, level1.json + images +sounds
"""
import pygame
from pygame.locals import *
import classes as cl
import constants as ct
import time
import pygame.freetype

pygame.init()
#loop speed limitation
pygame.time.Clock().tick(30)
icon=pygame.image.load(ct.icon())
pygame.display.set_icon(icon)

def menu():
     #menu_window = pygame.display.set_mode((ct.window_size(), ct.window_size()))
     #to be dev.
     level = "niveau1.json"
     return level    


def main():
     f=1
     while f:    
          pygame.time.Clock().tick(30)
          main_window = pygame.display.set_mode((ct.window_size()-20, ct.window_size()))
          font = pygame.freetype.SysFont("Comic Sans MS", 40, 0)
          main_window.fill((0,0,0))
          font.render_to(main_window, (80, 270), "PRESS SPACE TO PLAY", (255, 255, 255))
          pygame.display.set_caption("Mac Gyver Maze")
          pygame.display.flip()
          for event in pygame.event.get():
               if event.type == QUIT:
                         f=0
               if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         f=play(menu())

                    


def play(level):
     maze=cl.Maze(level)
     maze.load_level()
     gyver = cl.Character(maze.sprites)
     maze.display_maze(gyver.location, gyver.item_carried)
     son=pygame.mixer.Sound("MacGyver.ogg")
     i=1
     son.play()
     son.fadeout(10000)
     while i:    
          pygame.time.Clock().tick(30)
          for event in pygame.event.get():
               if event.type == QUIT:
                    son.stop()
                    return 0
               if event.type == KEYDOWN:
                    #key detection via real values (locals doesn't seems to be taken into account in dict)
                    switcher={
                         273: "up",
                         274: "down",
                         276: "left",
                         275: "right"
                         }
                    type=switcher.get(event.key)
                    #If value not within switcher dont use property
                    if type != None:
                         gyver.move(switcher.get(event.key))
                         #update of colected items +sprite + update of the carried-items 
                         for item in ct.items_to_collect():
                              if item == maze.sprites[gyver.location]:
                                   gyver.item_carried.append(maze.sprites[gyver.location])
                                   maze.sprites[gyver.location]=""
                         maze.display_maze(gyver.location, gyver.item_carried)
          #test of winning/loosing conditions
          if (gyver.location == maze.sprites.index("guard")) and (len(gyver.item_carried) == 
               len(ct.items_to_collect())):
               son.stop()
               win=pygame.mixer.Sound("0812.ogg")
               win.play()
               main_window = pygame.display.set_mode((ct.window_size(), ct.window_size()))
               font = pygame.freetype.SysFont("Comic Sans MS", 40, 0)
               main_window.fill((0,0,0))
               font.render_to(main_window, (205 , 270), "YOU WIN", (255, 255, 255))
               pygame.display.flip()
               time.sleep(4)
               win.stop()
               i=0
          elif (gyver.location == maze.sprites.index("guard")) and (len(gyver.item_carried) != 
               len(ct.items_to_collect())):
               son.stop()
               pygame.mixer.music.set_volume(0.2)
               pygame.mixer.music.load("round_end.wav")
               pygame.mixer.music.play()
               main_window = pygame.display.set_mode((ct.window_size(), ct.window_size()))
               font = pygame.freetype.SysFont("Comic Sans MS", 40, 0)
               main_window.fill((0,0,0))
               font.render_to(main_window, (180, 270), "GAME OVER", (255, 255, 255))
               pygame.display.flip()
               time.sleep(4)
               pygame.mixer.music.stop()
               i=0
     return 1

if __name__ == "__main__":
     main()

