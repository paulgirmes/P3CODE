
"""contient les adresses des images, 
pour une modification plus facile, le titre de la fenêtre, 
son icône, le nombre de sprites sur une largeur, 
la taille des sprites, et donc la taille de la fenêtre 
(multiplie les deux dernières constantes)."""



def sprite_dim():
    return 40

def items_to_collect():
    item_list = ["needle", "plastic_tube", "ether"]
    return item_list

def window_size():
    return 600

def img(img):
    switcher={
        "wall": "wall4040.png",
        "macgyver": "MacGyver.png",
        "guard": "Gardien.png",
        "": "floortile4040.png",
        "entry": "floortile4040.png",
        "needle": "aiguille.png",
        "plastic_tube": "tube_plastique.png",
        "ether": "ether.png"
        }
    return switcher.get (img)




