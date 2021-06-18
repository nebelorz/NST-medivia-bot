import pyautogui as pyAG            ## Inputs + hotkeys
import pydirectinput as pyDI        ## Direct inputs
from playsound import playsound     ## Play sounds

def rune_cast(self):
    print('* Start *')

    # Move cursor to blank rune
    pyAG.moveTo(rune_pos[0], rune_pos[1], 1, pyAG.easeInOutExpo)

    # Move blank rune to hand
    pyAG.mouseDown(button='left')
    pyAG.moveTo(hand_pos[0], hand_pos[1], 1, pyAG.easeInOutExpo)
    pyAG.mouseUp(button='left')

    # Cast spell on default channel
    pyAG.hotkey('altright','3')
    pyDI.write('s ' + self)
    pyDI.press('enter')
    playsound('sounds/add.wav')
    print('Casted:', self)

    # Move rune back to backpack
    pyAG.moveTo(hand_pos[0], hand_pos[1], 1, pyAG.easeInOutExpo)
    pyAG.mouseDown(button='left')
    pyAG.moveTo(rune_pos[0], rune_pos[1], 1, pyAG.easeInOutExpo)
    pyAG.mouseUp(button='left')

def spell_cast(self):
    print('* Start *')

    # Cast spell on default channel
    pyAG.hotkey('altright','3')
    pyDI.write('s ' + self)
    pyDI.press('enter')
    playsound('sounds/add.wav')
    print('Casted:', self)

def find_rune():
    global rune_pos
    rune_pos = pyAG.locateCenterOnScreen('images/blank_rune.png')
    if rune_pos == None:
        print('No blank rune found.')
        playsound('sounds/error.wav')
        return(False)
    else:
        return(True)

def find_hand(self):
    global hand_pos
    hand_pos = pyAG.locateCenterOnScreen('images/{}.png'.format(self))
    if hand_pos == None:
        print('The', self.replace('_', ' '), 'is not empty.')
        playsound('sounds/error.wav')
        return(False)
    else:
        return(True)

def find_food(self):
    global food
    food = pyAG.locateCenterOnScreen('images/{}.png'.format(self))
    if food == None:
        print('No', self.replace('_', ' '), 'found.')
        return(False)
    else:
        return(True)       

def mana():
    mid_mana = pyAG.locateCenterOnScreen('images/mid_mana.png')
    if mid_mana == None:
        print('You have less than half of your total mana.')
        playsound('sounds/error.wav')
        return(False)
    else:
        return(True)

def eat_food():
    pyAG.moveTo(food[0], food[1], 1, pyAG.easeInOutExpo)
    for _ in range(4):
        pyAG.rightClick()