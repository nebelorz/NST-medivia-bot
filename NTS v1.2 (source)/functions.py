import time
import pyautogui as pyAG            ## Inputs + hotkeys
import pydirectinput as pyDI        ## Direct inputs

def mana():
    mid_mana = pyAG.locateCenterOnScreen('images/mid_mana.png')
    if mid_mana == None:
        print('Less than half of your total mana.')
        return(False)
    else:
        return(True)

def rune_cast(self):
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
    print('Casted:', self)

    # Move rune back to backpack
    pyAG.moveTo(hand_pos[0], hand_pos[1], 1, pyAG.easeInOutExpo)
    pyAG.mouseDown(button='left')
    pyAG.moveTo(rune_pos[0], rune_pos[1], 1, pyAG.easeInOutExpo)
    pyAG.mouseUp(button='left')

def spell_cast(self):
    # Cast spell on default channel
    pyAG.hotkey('altright','3')
    pyDI.write('s ' + self)
    pyDI.press('enter')
    print('Casted:', self)

def move_ring():
    # Move cursor to ring
    pyAG.moveTo(boost_pos[0], boost_pos[1], 1, pyAG.easeInOutExpo)

    # Move ring to empty ring slot
    pyAG.mouseDown(button='left')
    pyAG.moveTo(empty_ring_pos[0], empty_ring_pos[1], 1, pyAG.easeInOutExpo)
    pyAG.mouseUp(button='left')

def find_rune():
    global rune_pos
    rune_pos = pyAG.locateCenterOnScreen('images/blank_rune.png')
    if rune_pos == None:
        print('No blank rune found.')
        return(False)
    else:
        return(True)

def find_hand(self):
    global hand_pos
    hand_pos = pyAG.locateCenterOnScreen('images/{}.png'.format(self))
    if hand_pos == None:
        print('The', self.replace('_', ' '), 'is not empty.')
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

def find_boost(self):
    global boost_pos
    boost_pos = pyAG.locateCenterOnScreen('images/{}.png'.format(self))
    if boost_pos == None:
        print('No', self.replace('_', ' '), 'found')
        return(False)
    else:
        return(True)

def find_empty_ring():
    global empty_ring_pos
    empty_ring_pos = pyAG.locateCenterOnScreen('images/ring_slot.png')
    if empty_ring_pos == None:
        print('The ring slot is not empty.')
        return(False)
    else:
        return(True)

def eat_food():
    pyAG.moveTo(food[0], food[1], 1, pyAG.easeInOutExpo)
    for _ in range(4):
        pyAG.rightClick()
    time.sleep(1)