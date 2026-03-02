import pygetwindow as gw
import pyautogui as pag
import time
from component import Component

class GravityWindowComponent(Component):
    def __init__(self, window, startTime):
        super().__init__("Gravity", window, startTime)

        self._gravity_constant = 9.81

    def _gravity(self, window):

        start_time = time.perf_counter()

        if (window.bottomright[1] < pag.size()[1]):
                window.moveRel(0, int(self._acceleration(time.perf_counter() - start_time)))
            

    def _acceleration(self, time):
        return 0.5 * self._gravity_constant * time**2
    
    def update(self):
        self._gravity(self.window)
