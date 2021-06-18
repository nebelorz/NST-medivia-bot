import time
import functions
import find_window
import os
import sys
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from playsound import playsound

# VARS
stopped = False

## Main window
main_window = tk.Tk()
main_window.title("NEBEL'S SLACKER TOOLS")
#main_window.iconbitmap('icon.ico')       # Icon
main_window.geometry('300x185')
main_window.resizable(width=False, height=False)
main_window.attributes('-topmost', True)

## Styling (ttk)
main_window.style = ttk.Style(main_window)
main_window.configure(background='antiqueWhite')


main_window.style.configure('TLabel', font=('Verdana', 8, 'bold'), background='antiqueWhite')
main_window.style.configure('TCheckbutton', font=('Verdana', 7), background='antiqueWhite')
main_window.style.configure('TRadiobutton', font=('Verdana', 7, 'italic'), background='antiqueWhite')

main_window.style.configure('footer.TLabel', font=('Verdana', 7, 'italic'), background='antiqueWhite')
main_window.style.configure('start.TButton', font=('Verdana', 8, 'bold'), background='black')
main_window.style.configure('stop.TButton', font=('Verdana', 8, 'bold'), background='red')

'''
# Menu bar
menu_bar = tk.Menu(main_window)
main_window.config(menu=menu_bar)
filemenu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=filemenu)
'''

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

### MAIN WINDOW WIDGETS ###
##// Empty row
empty1 = ttk.Label(main_window)
empty1.grid(column=0, row=6)

#// Spell textbox
def spell_entry():
    spell_name = spell_txt.get()
    return(spell_name)
# Label
spell_label = ttk.Label(main_window, text="SPELL")
spell_label.grid(column=0, row=1, sticky='w')
# Text box
spell_txt = ttk.Entry(main_window,width=18)
spell_txt.grid(column=0, row=2)

#// Checkbutton blank runes
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
blank_rune_check.grid(column=0, row=3)


#// Hand selection
def hand_entry():
    hand = hand_value.get()
    if hand == 1:
        return('left_hand')
    elif hand == 2:
        return('right_hand')
    else:
        print('No hand selected(?)')
        exit()
hand_value = tk.IntVar()
hand_value.set(1)   ## Check left_hand_check by default
# Label
hand_label = ttk.Label(main_window, text="HAND")
hand_label.grid(column=1, row=1, sticky='n')
# Radio button
left_hand_check = ttk.Radiobutton(main_window,
                                 text='Left Hand   ',
                                 variable=hand_value,
                                 value=1,)
left_hand_check.grid(column=1, row=2)

right_hand_check = ttk.Radiobutton(main_window,
                                  text='Right Hand',
                                  variable=hand_value,
                                  value=2,
                                  )
right_hand_check.grid(column=1, row=3)

#// Check time
def check_time_entry():
    try:
        global sleep_time
        sleep_time = int(check_time_txt.get())
        return(True)
    except:
        print('Enter a valid value in the CHECK box (integer numbers)')
        return(False)
# Label
check_time_label = ttk.Label(main_window, text="CHECK (secs)")
check_time_label.grid(column=2, row=1, sticky='e')
# Text box
check_time_txt = ttk.Entry(main_window, width=4)
check_time_txt.insert(-1, '300')
check_time_txt.grid(column=2, row=2)

#// Checkbutton minimize
def minimize_entry():
    return(minimize.get())

minimize = tk.IntVar() # 1 yes 0 no
minimize_check = ttk.Checkbutton(main_window, 
                                   text="minimize",
                                   variable=minimize,
                                   onvalue=1,
                                   offvalue=0,)
minimize_check.grid(column=2, row=3)

#// Food
def food_entry():
    food = food_value.get()
    if food == 1:
        return('fish')
    elif food == 2:
        return('ham')
    elif food == 3:
        return('brown_mushroom')
    else:
        print('No food selected(?)')
        exit()
food_value = tk.IntVar()
food_value.set(1)   ## Check option 1 by default
# Label
food_label = ttk.Label(main_window, text="FOOD")
food_label.grid(column=0, row=7, sticky='w')
# Radio button
fish_check = ttk.Radiobutton(main_window,
                                 text='Fish',
                                 variable=food_value,
                                 value=1)
fish_check.grid(column=0, row=8, sticky='w')
ham_check = ttk.Radiobutton(main_window,
                                 text='Ham (>5 hams)',
                                 variable=food_value,
                                 value=2,
                                 )
ham_check.grid(column=0, row=9, sticky='w')
brown_mushroom_check = ttk.Radiobutton(main_window,
                                 text='Brown Mushroom    ',
                                 variable=food_value,
                                 value=3)
brown_mushroom_check.grid(column=0, row=10, sticky='w')

#// Footer
# Label
footer = ttk.Label(main_window, text="slackertools@gmail.com",  style='footer.TLabel')
footer.grid(column=0, row=12)
footer = ttk.Label(main_window, text="v1.1",  style='footer.TLabel')
footer.grid(column=2, row=12, sticky='e')
## MISC FUNCTIONS
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

## Start button
# Start thread
def start_thread():
    start_thread =threading.Thread(target=start_button)
    start_thread.daemon = True
    start_thread.start()

def start_button():
    global stopped
    stopped = False

    # CHECK MEDIVIA EXISTS
    while find_window.check_window('Medivia') and stopped == False:
        print('start while')
        if check_time_entry() == False:
            play_sound('error')
            messagebox.showerror("Error", 'CHECK must be numbers.')
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
            else:
                functions.rune_cast(spell_entry())
                continue
    
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
                    
            # MINIMIZE WINDOW
            if minimize_entry() == 1:
                find_window.minimize_window('Medivia')

            # SLEEP + CONTINUE
            time.sleep(sleep_time)
            continue          

start_btn = ttk.Button(main_window,
                         text="Start",
                         style='start.TButton',
                         command=start_thread)
start_btn.grid(column=2,row=11)

## Stop button
def stop_button():
    global stopped
    stopped = True
    print('- Stopped -')

stop_btn = ttk.Button(main_window,
                         text="Stop",
                         style='stop.TButton',
                         command=stop_button)
stop_btn.grid(column=0,row=11)



spell_txt.focus_set()   ## Input focus on the spell box
main_window.mainloop()  ## Loops the window indefinetly