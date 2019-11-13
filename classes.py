import constants as ct

class Maze:
    def __init__(self, level):
        self.level=level
        self.sprites=[]
    
    def load_level(self):
        sprite = 0
        self.sprites.append(sprite)
        self.entrance = 0
    
    def display_maze(self, character_location):
        
        pass


class Character:
    def __init__(self, sprites):
        self.location=0
        self.item_carried=[]
        self.Position_px=(self.sprite_location)
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

            

