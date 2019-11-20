"""some constants for an easier modification"""


def sprite_dim():
    return 40


def items_to_collect():
    item_list = ["needle", "plastic_tube", "ether"]
    return item_list


def window_size():
    return 620


def img(img):
    switcher = {
        "wall": "images/wall4040.png",
        "macgyver": "images/MacGyver.png",
        "guard": "images/Gardien.png",
        "": "images/floortile4040.png",
        "entry": "images/floortile4040.png",
        "needle": "images/aiguille.png",
        "plastic_tube": "images/tube_plastique.png",
        "ether": "images/ether.png",
    }
    return switcher.get(img)


def icon():
    icon = "images/MacGyver.png"
    return icon
