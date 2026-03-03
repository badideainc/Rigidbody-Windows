from window_event import *
import pyautogui as pag
import ctypes

class ScreenListener:
    def __init__(self):
        self.windows = []
        self._listeners = []

    def add_window(self, window):
        self.windows.append(window)

        if window._has_event("onClick"):
            if (not self._has_listener(ScreenClickListener)):
                click_listener = ScreenClickListener(self)
                self._listeners.append(click_listener)
    
    def listen(self):
        while True:
            for window in self.windows:
                window.update()
            for listener in self._listeners:
                listener.listen()

    def _inframe(self, window, x, y):
        left, top, right, bottom = window.left, window.top, window.right, window.bottom
        return left <= x <= right and top <= y <= bottom
    
    def _has_listener(self, listener_type):
        for listener in self._listeners:
            if isinstance(listener, listener_type):
                return True
        return False

class ScreenClickListener:
    def __init__(self, screenListener):
        self.screenListener = screenListener
        self._was_left_down = False

    def listen(self):
        left_down = (ctypes.windll.user32.GetAsyncKeyState(0x01) & 0x8000) != 0
        if not left_down or self._was_left_down:
            self._was_left_down = left_down
            return

        x, y = pag.position()
        for window in self.screenListener.windows:
            if self.screenListener._inframe(window.window, x, y):
                event = WindowClickEvent(window.window, x, y)
                window.onClick(event)

        self._was_left_down = left_down
            