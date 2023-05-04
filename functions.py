import pyautogui as pyAG
import pydirectinput as pyDI

from random import uniform
from time import sleep
from get_window import *
from get_info import *


def disable_WASD():
    if image_exists('WASD'):
        wasd_pos = get_image_pos('WASD')
        pyAG.click(wasd_pos[0], wasd_pos[1])


def cast_spell(spell):
    disable_WASD()
    pyAG.hotkey('altright', '3')
    pyAG.write('s ' + spell)
    sleep(1)
    pyDI.press('enter')


def move_to_ring_slot(item):
    if image_exists('ringslot'):
        ringslot_pos = get_image_pos('ringslot')
        if image_exists(item):
            lifering_pos = get_image_pos('lifering')
            pyAG.moveTo(lifering_pos[0], lifering_pos[1])
            pyAG.mouseDown(button='left')
            pyAG.moveTo(ringslot_pos[0], ringslot_pos[1])
            pyAG.mouseUp(button='left')


def eat_food(item):
    if image_exists(item):
        food = get_image_pos(item)
        pyAG.moveTo(food[0], food[1])
        for clicks in range(5):
            pyAG.rightClick()


def logout():
    if image_exists('logoutbutton'):
        logout_button = get_image_pos('logoutbutton')
        pyAG.moveTo(logout_button[0], logout_button[1])
        pyAG.leftClick()
        if image_exists('logoutforce'):
            logout_force = get_image_pos('logoutforce')
            pyAG.moveTo(logout_force[0], logout_force[1])
            pyAG.leftClick()
