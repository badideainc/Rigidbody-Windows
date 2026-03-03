import subprocess
import time
import importlib
import pygetwindow as gw
from component import Component
import inspect

class RigidbodyWindow:
    def __init__(self, executable, windowName, components):
        self.window = self._open_window(executable, windowName)
        self.start_time = time.perf_counter()

        self.components = []

        for component in components:
            self.add_component(component)

        self.update()

    def _open_window(self, executable, windowName, timeout=5):
        subprocess.Popen([executable])  # start window
        deadline = time.time() + timeout

        while time.time() < deadline:
            wins = gw.getWindowsWithTitle(windowName)  # e.g., "Untitled - Notepad"
            if wins:
                win = wins[0]
                win.activate()
                return win
            time.sleep(0.05)

        raise RuntimeError("Could not find window")
    
    def add_component(self, component):
        module_name = component.removesuffix("Component")
        module_name = "".join([f"_{c.lower()}" if c.isupper() else c for c in module_name]).lstrip("_")
        module = importlib.import_module(module_name)
        class_ = getattr(module, component)
        self.components.append(class_(self.window, self.start_time))

    def update(self):
        for component in self.components:
                component.update()
            
    def onClick(self, event):
        for component in self.components:
            if self._overrides(component, "onClick"):
                component.onClick(event)

    def onEnterCollision(self, event):
        for component in self.components:
            if self._overrides(component, "onEnterCollision"):
                component.onEnterCollision(event)
    
    def onExitCollision(self, event):
        for component in self.components:
            if self._overrides(component, "onExitCollision"):
                component.onExitCollision(event)

    def _has_event(self, eventName):
        for component in self.components:
            if self._overrides(component, eventName):
                return True 
        return False
    
    def _overrides(self, component, eventName):
        return inspect.getattr_static(type(component), eventName, None) is not inspect.getattr_static(Component, eventName, None)

    def __str__(self):
        return f"RigidbodyWindow(window={self.window}, components={self.components})"