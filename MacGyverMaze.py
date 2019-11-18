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
     maze=cl.Maze(menu())
     maze.load_level()
     gyver=cl.Character(maze.sprites)
     maze.display_maze(gyver.location)
     son=pygame.mixer.Sound("MacGyver.ogg")
     i=1
     son.play()
     son.fadeout(10000)
     while i:    
          pygame.time.Clock().tick(30)
          for event in pygame.event.get():
               if event.type == QUIT:
                    i=0
               if event.type == KEYDOWN:
                    #key detection via real values (locals doesn't seems to be taken into account in dict)
                    switcher={
                         273: "up",
                         274: "down",
                         276: "left",
                         275: "right"
                         }
                    gyver.move(switcher.get(event.key))
                    #update of colected items +sprite + update of the carried-items 
                    for item in ct.items_to_collect():
                         if item == maze.sprites[gyver.location]:
                              gyver.item_carried.append(maze.sprites[gyver.location])
                              maze.sprites[gyver.location]=""
                    maze.display_maze(gyver.location)
          #test of winning/loosing conditions
          if (gyver.location == maze.sprites.index("guard")) and (len(gyver.item_carried) == 
               len(ct.items_to_collect())):
               pygame.display.set_caption("YOU WIN")
               win=pygame.mixer.Sound("0812.ogg")
               win.play()
               time.sleep(4)
               i=0
          elif (gyver.location == maze.sprites.index("guard")) and (len(gyver.item_carried) != 
               len(ct.items_to_collect())):
               pygame.display.set_caption("GAME OVER")
               pygame.mixer.music.set_volume(0.2)
               pygame.mixer.music.load("round_end.wav")
               pygame.mixer.music.play()
               time.sleep(4)
               i=0

if __name__ == "__main__":
     main()

