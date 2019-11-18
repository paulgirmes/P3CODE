"""some constants for an easier modification"""

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

def icon():
    icon="MacGyver.png"
    return icon




