import pygame
import json
import random
from pygame.locals import *
import constants as ct


class Maze:
    def __init__(self, level_file):
        self.level=level_file
        self.sprites=[]
    
    def load_level(self):
        #import du niveau à partir du fichier .json
        with open(self.level) as f:
            data=json.load(f)
            for entry in data:
                self.sprites.append(entry["sprites"])
        empty_sprites_index=[]
        index_sprites=0
        while index_sprites < len(self.sprites):
            if self.sprites[index_sprites] == "":
                empty_sprites_index.append(index_sprites)
            index_sprites +=1
        items_to_collect=ct.items_to_collect()
        for n in items_to_collect:
            random_index=random.randint(0, len(empty_sprites_index)-1)
            self.sprites[empty_sprites_index[random_index]]=n
            empty_sprites_index.pop(random_index)
        return self.sprites


            
        
    def display_maze(self, character_position_px):
        
        pass


class Character:
    def __init__(self, sprites):
        self.location=0
        self.item_carried=[]
        self.Position_px=(self.location)
        self.sprites=sprites
   
    def move(self, direction):
        switcher = {
            "up": (-1*ct.maze_dim),
            "down": ct.maze_dim,
            "right": 1,
            "left":  -1}

        new_location=switcher.get(int(direction)) + self.location
        if (new_location <= len(self.sprites-1) and new_location >= 0 
            and self.sprites[new_location] != "wall"):
            self.sprite_location = new_location
            if self.sprites[self.location] != "":
                self.item_carried.append(self.sprites[self.location])

            

