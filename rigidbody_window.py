import webview
import time
import importlib
import pygetwindow as gw
from component import Component
import inspect
from window_math import Vector2
from pathlib import Path

class RigidbodyWindow:
    def __init__(self, windowName, launchPath, components, position = Vector2(0, 0)):
        self.screen = webview.screens[0]
        self.window = self._open_window(launchPath, windowName)

        self.window.move(position.x, position.y)
        self.start_time = time.perf_counter()

        self.components = []

        for component in components:
            self.add_component(component)

        self.update()

    def _open_window(self, path, windowName):
        url = path.resolve().as_uri()

        window = webview.create_window(windowName, url=url)

        if window is None:
            raise RuntimeError("Could not find window")
        
        webview.start()

        return window      
    
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