from rigidbody_window import RigidbodyWindow
from screen_listener import ScreenListener
from pathlib import Path

listener = ScreenListener()
html_path = Path(__file__).parent / "test.html"

rb = RigidbodyWindow("test.html", "Test", html_path, ["GravityWindowComponent"])
print(rb)

listener.add_window(rb)
listener.listen()