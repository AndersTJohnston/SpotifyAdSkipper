from win32gui import GetWindowText, FindWindow
from win32api import SendMessage
from win32con import WM_CLOSE
from subprocess import Popen
from time import sleep
from pathlib import Path
from pyautogui import press
from pygetwindow import getWindowsWithTitle, getActiveWindowTitle
from getpass import getuser

window_name: str = "Spotify Free" # Name of application
application_path: Path | None = None # Path to the exe of your application, none to use default
cycle_time: float | int = 0.1 # Time in seconds between checking if an ad is playing. Increase to reduce effect on cpu

if not application_path:
    application_path = Path("C:/Users") / getuser() / "AppData/Roaming/Spotify/Spotify.exe"

def main() -> None:
    """Runs the main program"""
    hwnd = FindWindow(None, window_name)
    if hwnd == 0:
        print(f"\"{window_name}\" is not currently open or does not exist.")
    else:
        print("Skipping ads.")
        while True:
            window_text = GetWindowText(hwnd)
            if not " - " in window_text and not window_name in window_text:
                prev_window = getActiveWindowTitle()
                SendMessage(hwnd, WM_CLOSE, 0, 0)
                sleep(0.1)
                Popen(application_path)
                while not window_text:
                    sleep(0.1)
                sleep(2)
                press("playpause")
                getWindowsWithTitle(prev_window)[0].activate()

            sleep(cycle_time)

if __name__ == "__main__":
    main()