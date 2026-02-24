import pygetwindow as gw
import pyautogui as pag
import time

def gravity(window):

    start_time = time.perf_counter()

    while window:
        if (window.bottomright[1] < pag.size()[1]):
            window.moveRel(0, int(acceleration(time.perf_counter() - start_time)))

def acceleration(time):
    return 0.5 * 9.81 * time**2

win = gw.getWindowsWithTitle('Untitled')[0]
gravity(win)