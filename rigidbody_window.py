import subprocess
import time
import importlib
import pygetwindow as gw

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
        self.update()

    def __str__(self):
        return f"RigidbodyWindow(executable={self.executable}, window={self.window}, components={self.components})"

rb = RigidbodyWindow("notepad.exe", "Untitled - Notepad", ["GravityWindowComponent"])
print(rb)