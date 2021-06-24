import time
import threading
import tkinter as tk
import keyboard
import functions
import find_window
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from playsound import playsound

# VARS
stopped = True

## Main window
main_window = ThemedTk(theme='plastik')
main_window.title("NST")
main_window.iconbitmap('icon.ico') #Icon
main_window.geometry('215x270')
main_window.resizable(width=False, height=False)
main_window.attributes('-topmost', True)

## Styling (ttk)
main_window.style = ttk.Style(main_window)
main_window.configure(background='antiqueWhite2')

main_window.style.configure('TLabel', font=('Verdana', 8, 'bold'), background='antiqueWhite2')
main_window.style.configure('TCheckbutton', font=('Verdana', 7), background='antiqueWhite2')
main_window.style.configure('TRadiobutton', font=('Verdana', 7, 'italic'), background='antiqueWhite2')

main_window.style.configure('footer.TLabel', font=('Verdana', 7, 'italic'), background='antiqueWhite2')
main_window.style.configure('start.TButton', font=('Verdana', 8, 'bold'))
main_window.style.configure('stop.TButton', font=('Verdana', 8, 'bold'))

## MISC FUNCTIONS ##
def play_sound(self):
    try:
        if self == 'error':
            playsound('sounds/error.wav')
        elif self == 'add':
            playsound('sounds/add.wav')
        elif self == 'bought':
            playsound('sounds/bought.wav')
        elif self == 'ok':
            playsound('sounds/ok.wav')
    except:
        print('This sound doesnt exist')

### MAIN WINDOW WIDGETS ###
## Spell textbox
def spell_entry():
    spell_name = spell_txt.get()
    return(spell_name)
#Label
spell_label = ttk.Label(main_window, text="SPELL")
spell_label.grid(column=0, row=1, sticky='nw', padx=2)
#Text box
spell_txt = ttk.Entry(main_window,width=18)
spell_txt.grid(column=0, row=2, sticky='nw', padx=2)
#Checkbutton blank runes
def blank_rune_entry():
    blank_value = (blank_rune.get())
    if blank_value == 0:
        return(False)
    elif blank_value == 1:
        return(True)
blank_rune = tk.IntVar() # 1 yes 0 no
blank_rune_check = ttk.Checkbutton(main_window, 
                                   text="needs blank rune",
                                   variable=blank_rune,
                                   onvalue=1,
                                   offvalue=0)
blank_rune_check.grid(column=0, row=3, sticky='nw', padx=1, pady=2)


## Hand selection
def hand_entry():
    hand = hand_cb.get()
    if hand == 'Left':
        return('left_hand')
    elif hand == 'Right':
        return('right_hand')
    else:
        print('No hand selected(?)')
        exit()
#Label
hand_label = ttk.Label(main_window, text="HAND")
hand_label.grid(column=0, row=1, sticky='nw', padx=125)
#Combobox
hand_cb = ttk.Combobox(main_window, values=['Left', 'Right'], state='readonly', width=5)
hand_cb.current(0)
hand_cb.bind("<<ComboboxSelected>>", lambda a : hand_cb.selection_clear())  # Clear selection
hand_cb.grid(column=0, row=2, sticky='nw', padx=125)


## Food
def food_entry():
    food = food_cb.get()
    if food == 'Fish':
        return('fish')
    elif food == 'Ham':
        return('ham')
    elif food == 'Meat':
        return('meat')
    elif food == 'Brown Mushroom':
        return('brown_mushroom')
    else:
        print('No food selected(?)')
        exit()
#Label
food_label = ttk.Label(main_window, text="FOOD")
food_label.grid(column=0, row=5, sticky='nw', padx=2)
#Combobox
food_cb = ttk.Combobox(main_window, values=['Ham', 'Fish', 'Meat', 'Brown Mushroom'], state='readonly', width=15)
food_cb.current(0)
food_cb.bind("<<ComboboxSelected>>", lambda a : food_cb.selection_clear())  # Clear selection
food_cb.grid(column=0, row=6, sticky='nw', padx=2)

## Separator
separator1 = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator1.grid(column=0, row=7, columnspan=3, sticky='ew', pady=8)

## Boost settings
def boost_entry():
    boost = boost_cb.get()
    if boost == 'Life Ring':
        return('life_ring')
    else:
        print('No boost selected')
        return(False)
#Label
boost_label = ttk.Label(main_window, text="BOOST")
boost_label.grid(column=0, row=8, sticky='nw', padx=2)
#Combobox
boost_cb = ttk.Combobox(main_window, values=['None', 'Life Ring'], state='readonly', width=15)
boost_cb.current(0)
boost_cb.bind("<<ComboboxSelected>>", lambda a : boost_cb.selection_clear())  # Clear selection
boost_cb.grid(column=0, row=9, sticky='nw', padx=2)

## Separator
separator2 = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator2.grid(column=0, row=10, columnspan=3, sticky='ew', pady=8)

## Check time
def check_time_entry():
    try:
        global sleep_time
        sleep_time = int(check_time_txt.get())
        return(True)
    except:
        print('Enter a valid value in the CHECK box (integer numbers)')
        return(False)
#Label
check_time_label = ttk.Label(main_window, text="CHECK (s)")
check_time_label.grid(column=0, row=11, sticky='nw', padx=2)
#Text box
check_time_txt = ttk.Entry(main_window, width=5)
check_time_txt.insert(-1, '300')
check_time_txt.grid(column=0, row=12, sticky='nw', padx=2)
#Checkbutton minimize
def minimize_entry():
    return(minimize.get())
minimize = tk.IntVar() # 1 yes 0 no
minimize_check = ttk.Checkbutton(main_window, 
                                   text="minimize",
                                   variable=minimize,
                                   onvalue=1,
                                   offvalue=0,)
minimize_check.grid(column=0, row=12, sticky='nw', padx=40, pady=5)

## Separator
separator3 = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator3.grid(column=0, row=14, columnspan=3, sticky='ew', pady=8)


## Start button
#Start thread
def start_thread():
    start_thread = threading.Thread(target=start_button)
    start_thread.daemon = True
    start_thread.start()

def start_button():
    global stopped
    stopped = False
    # CHECK MEDIVIA EXISTS
    while find_window.check_window('Medivia') == True:

        if check_time_entry() == False:
            play_sound('error')
            messagebox.showerror("Error", 'CHECK must be numbers.')
            break
        elif find_window.check_window('Medivia') == False:
            play_sound('error')
            messagebox.showerror("Error", 'Medivia not found.')
            break
        else: 
            find_window.get_window('Medivia')

        ## CAST
        while functions.mana() == True and stopped == False:
            if blank_rune_entry() == False:
                functions.spell_cast(spell_entry())
                continue
            elif functions.find_rune() == False and blank_rune_entry() == True:
                play_sound('error')
                messagebox.showwarning("Error", 'No blank runes found.')
                stopped = True
                break
            elif functions.find_hand(hand_entry()) == False and blank_rune_entry() == True:
                play_sound('error')
                messagebox.showwarning("Error", 'Selected hand must be free.')
                stopped = True
                break
            elif blank_rune_entry() == True:
                functions.rune_cast(spell_entry())
                continue
            else:
                play_sound('error')
                messagebox.showwarning("!!", 'Something went wrong (?).')
                stopped = True
                break

        else:
            if stopped == True:
                break
            else:
                if functions.find_food(food_entry()) == False:
                    play_sound('error')
                    messagebox.showwarning("Error", 'No food found.')
                    break
                else:
                    functions.eat_food()

                if functions.find_boost(boost_entry()) != False:
                    if boost_entry() == 'life_ring' and functions.find_empty_ring() == True:
                        functions.move_ring()
                    else:
                        play_sound('error')
                        messagebox.showwarning("Error", 'No life ring found.')
                        break

            # MINIMIZE WINDOW
            if minimize_entry() == 1:
                find_window.minimize_window('Medivia')

            # SLEEP + CONTINUE
            time.sleep(sleep_time)
            continue
    else:
        print('No Medivia found.')
        play_sound('error')
            
start_btn = ttk.Button(main_window,
                         text="Start",
                         style='start.TButton',
                         command=start_thread)
start_btn.grid(column=0,row=15, sticky='ne', padx=120)

## Stop button
def stop_button():
    global stopped
    stopped = True
    print('- Stopped -')
stop_btn = ttk.Button(main_window,
                         text="Stop",
                         style='stop.TButton',
                         command=stop_button)
stop_btn.grid(column=0, row=15, sticky='nw', padx=5)

## Footer
#Label
footer = ttk.Label(main_window, text="slackertools@gmail.com",  style='footer.TLabel')
footer.grid(column=0, row=20, sticky='sw', padx=2, pady=5)
footer = ttk.Label(main_window, text="v1.2",  style='footer.TLabel')
footer.grid(column=0, row=20, sticky='se', padx=120, pady=5)

## HOTKEYS
keyboard.add_hotkey('home', lambda: start_button())
keyboard.add_hotkey('end', lambda: stop_button())

spell_txt.focus_set()   ## Input focus on the spell box
main_window.mainloop()  ## Loops the window indefinetly