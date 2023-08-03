import sys
import time
import threading
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
from get_window import *
from get_info import *
from functions import *


# Main window
main_window = ThemedTk(theme='plastik')
main_window.title('[NST v1.4.1]')
main_window.iconbitmap('images/icon.ico')
main_window.geometry('300x415')
main_window.attributes('-topmost', True)

# Styling (ttk)
main_window.style = ttk.Style(main_window)
main_window.configure(background='antiqueWhite2')

main_window.style.configure('TLabel', font=(
    'Verdana', 8, 'bold'), background='antiqueWhite2')
main_window.style.configure('TCheckbutton', font=(
    'Verdana', 7), background='antiqueWhite2')
main_window.style.configure('TRadiobutton', font=(
    'Verdana', 7, 'italic'), background='antiqueWhite2')

main_window.style.configure('footer.TLabel', font=(
    'Verdana', 7, 'italic'), background='antiqueWhite2')
main_window.style.configure('start.TButton', font=('Verdana', 8, 'bold'))
main_window.style.configure('exit.TButton', font=('Verdana', 8, 'bold'))

# FUNCTIONS
def spell_entry():
    if spell_input.get():
        return spell_input.get()


def blank_rune_entry():
    blank_value = (blank_rune.get())
    return blank_value != 0


def food_entry():
    food = food_cb.get()
    if food == 'Ham':
        return 'hams'
    elif food == 'Brown Mushroom':
        return 'brownmushroom'
    elif food == 'Fish':
        return 'fish'


def boost_entry():
    boost = boost_cb.get()
    if boost == 'Life Ring':
        return 'lifering'


def time_entry():
    try:
        wait_time = int(time_input.get()) * 60
        if wait_time > 0:
            return wait_time
        else:
            return None
    except:
        return None


def minimize_entry():
    minimize_value = minimize.get()
    return minimize_value != 0


def logout_entry():
    logout_value = logout_checkbox.get()
    return logout_value != 0


def thread_1():
    start_thread = threading.Thread(target=start_button)
    start_thread.daemon = True
    start_thread.start()


def start_button():
    main_window.iconbitmap('images/iconplay.ico')

    while True:
        if get_window():
            if not spell_entry():
                messagebox.showerror('ERROR!', 'Spell input should be filled.')
                break

            if not time_entry():
                messagebox.showerror(
                    'ERROR!', "Time only accept integer numbers.")
                break

            if blank_rune_entry() and not image_exists('blankrune'):
                if logout_entry():
                    logout()
                messagebox.showwarning('WARNING!', 'Blank runes not found.')
                break

            if not food_entry() or not image_exists(food_entry()):
                if logout_entry():
                    logout()
                messagebox.showwarning('WARNING!', 'Food not found.')
                break

            if not boost_entry():
                pass
            elif not image_exists(boost_entry()):
                if logout_entry():
                    logout()
                messagebox.showwarning('WARNING!', 'Boost item not found.')
                break

            while not image_exists('not_enough_mana'):
                if blank_rune_entry() and not image_exists('blankrune'):
                    break
                cast_spell(spell_entry())

            eat_food(food_entry())

            if boost_entry():
                move_to_ring_slot(boost_entry())

            if minimize_entry():
                minimize_window()

            if time_entry():
                time.sleep(time_entry())

        else:
            messagebox.showerror('ERROR!', 'Medivia is not running.')
            break

    main_window.iconbitmap('images/icon.ico')


def exit_button():
    sys.exit()


### MAIN WINDOW WIDGETS ###
# SPELL TEXTBOX
spell_label = ttk.Label(main_window, text="SPELL")
spell_label.grid(column=0, row=1, sticky='nw', padx=2, pady=5)

spell_input = ttk.Entry(main_window, width=18)
spell_input.grid(column=0, row=2, sticky='nw', padx=2)


# BLANK RUNES CHECKBOX
blank_rune = tk.IntVar()
blank_rune_checkbox = ttk.Checkbutton(main_window,
                                      text="needs blank rune",
                                      variable=blank_rune,
                                      onvalue=1,
                                      offvalue=0)
blank_rune_checkbox.grid(column=0, row=3, sticky='nw', padx=5, pady=5)

# Separator
separator1 = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator1.grid(column=0, row=4, ipadx=140, padx=5, pady=10, sticky="w")

# FOOD SELECT
food_label = ttk.Label(main_window, text="FOOD")
food_label.grid(column=0, row=5, sticky='nw', padx=2, pady=5)

food_cb = ttk.Combobox(main_window, values=[
                       'Ham', 'Fish', 'Brown Mushroom'], state='readonly', width=15)
food_cb.current(0)
food_cb.bind("<<ComboboxSelected>>", lambda a: food_cb.selection_clear())
food_cb.grid(column=0, row=6, sticky='nw', padx=2)

# Separator
separator1 = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator1.grid(column=0, row=7, ipadx=140, padx=5, pady=10, sticky="w")


# BOOST SELECT
boost_label = ttk.Label(main_window, text="BOOST")
boost_label.grid(column=0, row=8, sticky='nw', padx=2, pady=5)

boost_cb = ttk.Combobox(main_window, values=[
                        None, 'Life Ring'], state='readonly', width=15)
boost_cb.current(0)
boost_cb.bind("<<ComboboxSelected>>", lambda a: boost_cb.selection_clear())
boost_cb.grid(column=0, row=9, sticky='nw', padx=2)

# Separator
separator2 = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator2.grid(column=0, row=10, ipadx=140, padx=5, pady=10, sticky="w")

# SETTINGS
settings_label = ttk.Label(main_window, text="SETTINGS")
settings_label.grid(column=0, row=11, sticky='nw', padx=2, pady=5)

# TIME INPUT
time_input = ttk.Entry(main_window, width=2)
time_input.insert(-1, '2')
time_input.grid(column=0, row=12, sticky='nw', padx=2)

time_label = ttk.Label(main_window, text='minutes between checks')
time_label.config(font=('Verdana', 7))
time_label.grid(column=0, row=12, sticky='w', padx=25, pady=5)

# MINIMIZE CHECKBOX
minimize = tk.IntVar()
minimize_check = ttk.Checkbutton(main_window,
                                 text="minimize",
                                 variable=minimize,
                                 onvalue=1,
                                 offvalue=0,)
minimize_check.grid(column=0, row=13, sticky='nw', padx=2, pady=4)

# LOGOUT CHECKBOX
logout_checkbox = tk.IntVar()
logout_check = ttk.Checkbutton(main_window,
                               text="logout if no supplies",
                               variable=logout_checkbox,
                               onvalue=1,
                               offvalue=0,)
logout_check.grid(column=0, row=14, sticky='nw', padx=2)

# Separator
separator3 = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator3.grid(column=0, row=15, ipadx=140, padx=5, pady=10, sticky="w")

# START BUTTON
start_btn = ttk.Button(main_window,
                       text="Start",
                       style='start.TButton',
                       command=thread_1)
start_btn.grid(column=0, row=16, sticky='ne', padx=195)

# EXIT BUTTON
exit_btn = ttk.Button(main_window,
                      text="Exit",
                      style='exit.TButton',
                      command=exit_button)
exit_btn.grid(column=0, row=16, sticky='nw', padx=5)


main_window.mainloop()
