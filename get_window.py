import time
import pygetwindow as pyGW


def get_window():
    try:
        window = pyGW.getWindowsWithTitle('Medivia')[0]
        if window.isMinimized:
            window.restore()
            window.activate()
            window.maximize()
            time.sleep(1)
        else:
            window.activate()
            window.maximize()
            time.sleep(1)
        return True
    except IndexError:
        return False


def minimize_window():
    window = pyGW.getWindowsWithTitle('Medivia')[0]
    window.minimize()
