import pygetwindow as gw

def gravity(window):

    while window:
        if (window.bottomright[1] < 2000):
            window.move(0, 1)

win = gw.getWindowsWithTitle('Untitled')[0]

gravity(win)