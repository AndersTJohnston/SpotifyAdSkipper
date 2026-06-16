from win32gui import GetWindowText, FindWindow, IsWindow
from win32api import SendMessage
from win32con import WM_CLOSE
from subprocess import Popen
from time import sleep
from pathlib import Path
from pyautogui import press

window_name = "Spotify Free" # Name of application
application_path = Path("C:/Users/ander/AppData/Roaming/Spotify/Spotify.exe") # Path to the exe of your application
cycle_time = 0.1 # Time in seconds between checking if an ad is playing. Increase to reduce effect on cpu


def main() -> None:
    """Runs the main program"""
    hwnd = FindWindow(None, window_name)
    if hwnd == 0:
        print(f"\"{window_name}\" is not currently open or does not exist.")
    else:
        print("Skipping ads.")
        while True:
            window_text = GetWindowText(hwnd)
            if not " - " in window_text and window_text != window_name:
                SendMessage(hwnd, WM_CLOSE, 0, 0)
                sleep(0.1)
                Popen(application_path)
                while not window_text:
                    sleep(0.1)
                sleep(2)
                press("playpause")

            sleep(cycle_time)

if __name__ == "__main__":
    main()