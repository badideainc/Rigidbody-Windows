from rigidbody_window import RigidbodyWindow
from screen_listener import ScreenListener
from pathlib import Path

listener = ScreenListener()
html_path = Path(__file__).parent / "windows/test.html"

rb = RigidbodyWindow("Test", html_path, ["GravityWindowComponent"])
print(rb)

listener.add_window(rb)
listener.listen()