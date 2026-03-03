from rigidbody_window import RigidbodyWindow
from screen_listener import ScreenListener

listener = ScreenListener()

rb = RigidbodyWindow("notepad.exe", "Untitled - Notepad", ["GravityWindowComponent"])
print(rb)

listener.add_window(rb)
listener.listen()