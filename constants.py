
"""contient les adresses des images, 
pour une modification plus facile, le titre de la fenêtre, 
son icône, le nombre de sprites sur une largeur, 
la taille des sprites, et donc la taille de la fenêtre 
(multiplie les deux dernières constantes)."""


def maze_dim():
    return 15
def sprite_dim():
    return 50
def items_to_collect():
    needle = "filenameNeedle"
    plastic_tube = "filenameTube"
    ether = "filenameEther"
    item_list = [needle, plastic_tube, ether]
    return item_list
def cote_fenetre():
    return 500
def image_icone():
    return "dk_bas.png"
def titre_fenetre():
    return "dk_bas.png"

