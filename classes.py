"""
Class definitions for MacGyverMaze.py
"""

import pygame
import json
import random
from pygame.locals import *
import constants as ct
from math import sqrt


class Maze:
    """ returns an object of class Maze"""

    def __init__(self, level_file):
        """initiate the maze object, take a .JSON level file as arg. assign it to self.level
            Json file must only contain objects within the switcher of ct.img() 
            and of a number that returns an int when square rooted
        """
        self.level = level_file
        self.sprites = []

    def load_level(self):
        """load self.level keys 'sprites' in self.sprites[]
            detects 'free sprites' indexes
            randomly replaces 'free srites' of self.sprites with an item of ct.items_to_collect() 
        """
        # level import from JSON file
        with open(self.level) as f:
            data = json.load(f)
            for entry in data:
                self.sprites.append(entry["sprites"])
        empty_sprites_index = []
        index_sprites = 0
        # empty sprites index detection/storage
        while index_sprites < len(self.sprites):
            if self.sprites[index_sprites] == "":
                empty_sprites_index.append(index_sprites)
            index_sprites += 1
        # pseudo random insertion of items in free sprites lefts
        items_to_collect = ct.items_to_collect()
        for n in items_to_collect:
            random_index = random.randint(0, len(empty_sprites_index) - 1)
            self.sprites[empty_sprites_index[random_index]] = n
            empty_sprites_index.pop(random_index)

    def display_maze(self, character_pos_sprite, items_carried):
        """
        takes the character position as an int and the items carried by character as a list for arg.
        returns a window with the maze+character+items collected
        self.sprites[] must first be initiated once by self.load_level)
    
        """
        game_window = pygame.display.set_mode((ct.window_size() - 20, ct.window_size()))
        hero = pygame.image.load(ct.img("macgyver")).convert_alpha()
        # sprites img loading /postioning(from sprites number root and a sprite dim) + blit
        i = 0
        while i < len(self.sprites):
            item = self.sprites[i]
            image = self.sprite(i)
            image = pygame.image.load(ct.img(item)).convert_alpha()
            game_window.blit(
                image,
                (
                    (i % self.side_sprites_number() * ct.sprite_dim()),
                    (i // self.side_sprites_number() * ct.sprite_dim()),
                ),
            )
            i += 1
        # hero postion update
        game_window.blit(
            hero,
            (
                (character_pos_sprite % self.side_sprites_number() * ct.sprite_dim()),
                (character_pos_sprite // self.side_sprites_number() * ct.sprite_dim()),
            ),
        )
        font = pygame.freetype.SysFont("courrier", 15, 1)
        font.render_to(
            game_window,
            (125, 602),
            "Items collected: " + str(items_carried),
            (255, 255, 255),
        )
        pygame.display.flip()

    def side_sprites_number(self):
        """
        returns the square root of items number contained in self.sprites
        """
        side_sprites = sqrt(int(len(self.sprites)))
        return side_sprites

    def sprite(self, i):
        """
        takes an int returns a string as of "image" appended by that int
        """
        return "image" + str(i)


class Character:
    """
    returns an object af class Character
    """

    def __init__(self, sprites):
        """
        takes sprites as a list (from an instance of Maze)
        initiate the first position of the character+the items it carries
        """
        self.location = sprites.index("entry")
        self.item_carried = []
        self.char_sprites = sprites

    def move(self, direction):
        """
        takes a string and change self.location depending an maze's dimensions
        """
        switcher = {
            "up": -self.side_sprites_number(),
            "down": self.side_sprites_number(),
            "right": 1,
            "left": -1,
        }

        new_location = switcher.get(direction) + self.location
        # test to avoid exeeding maze's sprites dimension and to teleport through walls!
        if (
            new_location <= (len(self.char_sprites) - 1)
            and new_location >= 0
            and self.char_sprites[new_location] != "wall"
        ):
            # test to avoid "warping" between left-right ends of maze when not walls
            if (
                direction == "right" or direction == "left"
            ) and self.location // self.side_sprites_number() != new_location // self.side_sprites_number():
                pass
            else:
                self.location = new_location

    def side_sprites_number(self):
        """
        returns the square root of items number contained in self.sprites
        """
        side_sprites = sqrt(len(self.char_sprites))
        return int(side_sprites)
