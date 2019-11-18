import pygame
import json
import random
from pygame.locals import *
import constants as ct
from math import sqrt


class Maze:
    def __init__(self, level_file):
        self.level=level_file
        self.sprites=[]
        #self.side_sprites_number=15#sqrt(int(len(self.sprites)))
    
    def load_level(self):
        #level import from JSON file
        with open(self.level) as f:
            data=json.load(f)
            for entry in data:
                self.sprites.append(entry["sprites"])
        empty_sprites_index=[]
        index_sprites=0
        #empty sprites index detection/storage
        while index_sprites < len(self.sprites):
            if self.sprites[index_sprites] == "":
                empty_sprites_index.append(index_sprites)
            index_sprites +=1
        #pseudo random insertion of items in free sprites lefts
        items_to_collect=ct.items_to_collect()
        for n in items_to_collect:
            random_index=random.randint(0, len(empty_sprites_index)-1)
            self.sprites[empty_sprites_index[random_index]]=n
            empty_sprites_index.pop(random_index)
          
    def display_maze(self, character_pos_sprite):
        
        game_window = pygame.display.set_mode((ct.window_size(), ct.window_size()))
        hero=pygame.image.load(ct.img("macgyver")).convert_alpha()
        #sprites img loading /postioning(from sprites number root and a sprite dim) + blit 
        i=0
        while i < len(self.sprites):
            item = self.sprites[i]
            image=self.sprite(i)               
            image=pygame.image.load(ct.img(item)).convert_alpha()
            game_window.blit(image, ((i %self.side_sprites_number()*ct.sprite_dim()), (i//self.side_sprites_number()*ct.sprite_dim())))
            i += 1  
        #hero postion update
        game_window.blit(hero, ((character_pos_sprite%self.side_sprites_number()*ct.sprite_dim()), (character_pos_sprite//self.side_sprites_number()*ct.sprite_dim())))
        pygame.display.flip()
    
    def side_sprites_number(self):
        side_sprites=sqrt(int(len(self.sprites)))
        return side_sprites
    
    def sprite(self, i):
        return "image"+str(i)

class Character:
    def __init__(self, sprites):
        self.location=sprites.index("entry")
        self.item_carried=[]
        self.char_sprites=sprites
        #self.side_sprites_number=15#sqrt(int(len(self.sprites)))

   
    def move(self, direction):
        switcher = {
            "up": -self.side_sprites_number(),
            "down": self.side_sprites_number(),
            "right": 1,
            "left":  -1}

        new_location=switcher.get(direction) + self.location
        #test to avoid exeeding maze's sprites dimension and to go teleport through walls
        if (new_location <= (len(self.char_sprites)-1) and new_location >= 0 
            and self.char_sprites[new_location] != "wall"):
                #test to avoid "warping" between left-right ends
                if ((direction == "right" or direction == "left") and self.location//self.side_sprites_number() != new_location//self.side_sprites_number()):
                    pass
                else:
                    self.location = new_location

    def side_sprites_number(self):
        side_sprites=sqrt(len(self.char_sprites))
        return int(side_sprites)
                



            

