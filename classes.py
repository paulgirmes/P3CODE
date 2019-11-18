import pygame
import json
import random
from pygame.locals import *
import constants as ct
import math


class Maze:
    def __init__(self, level_file):
        self.level=level_file
        self.sprites=[]
        self.side_sprites_number=15#math.sqrt(int(len(self.sprites)))
    
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
          
    def display_maze(self, character_pos_sprite):
        game_window = pygame.display.set_mode((ct.window_size(), ct.window_size()))
        #balayage des sprites pour charger l'image correspondante et la coller/positionner(le nombre d'entrees "sprites du fichier niveau détermine le nombre de sprites au total") 
        i=0
        while i < len(self.sprites):
            item = self.sprites[i]
            image=sprite(i)
            image=pygame.image.load(ct.img(item)).convert_alpha()
            game_window.blit(image, ((i %self.side_sprites_number*ct.sprite_dim()), (i//self.side_sprites_number*ct.sprite_dim())))
            i += 1
        hero=pygame.image.load(ct.img("macgyver")).convert_alpha()
        game_window.blit(hero, ((character_pos_sprite%self.side_sprites_number*ct.sprite_dim()), (character_pos_sprite//self.side_sprites_number*ct.sprite_dim())))
        pygame.display.flip()
    

class Character:
    def __init__(self, sprites):
        self.location=sprites.index("entry")
        self.item_carried=[]
        self.char_sprites=sprites
        self.side_sprites_number=15#math.sqrt(int(len(self.sprites)))

   
    def move(self, direction):
        switcher = {
            "up": -self.side_sprites_number,
            "down": self.side_sprites_number,
            "right": 1,
            "left":  -1}

        new_location=switcher.get(direction) + self.location
        if (new_location <= (len(self.char_sprites)-1) and new_location >= 0 
            and self.char_sprites[new_location] != "wall"):
            self.location = new_location
        
            
            

def sprite(i):
    return "image"+str(i)

            

