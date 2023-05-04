import pyautogui as pyAG

from get_window import *


def get_image_pos(name):
    return pyAG.locateCenterOnScreen(f'images/{name}.jpg', confidence='0.9')


def image_exists(name):
    if pyAG.locateOnScreen(f'images/{name}.jpg', confidence='0.9') is not None:
        return True
