from win32gui import GetWindowText, FindWindow, SetWindowPos
from win32api import SendMessage
from win32con import WM_CLOSE, HWND_BOTTOM, SWP_NOMOVE, SWP_NOSIZE, SWP_NOACTIVATE
from subprocess import Popen
from time import sleep
from pathlib import Path
from pyautogui import press
from getpass import getuser

window_name: str = "Spotify Free" # Name of application
application_path: Path | None = None # Path to the exe of your application, none to use default
cycle_time: float | int = 0.1 # Time in seconds between checking if an ad is playing. Increase to reduce effect on cpu
wait_after_open: float | int = 1.5 # Time in seconds to wait after opening the window to playing the music; lower numbers may not work but will be faster

if not application_path: # Set default path
    application_path = Path("C:/Users") / getuser() / "AppData/Roaming/Spotify/Spotify.exe"

def main() -> None:
    """Runs the main program"""
    hwnd = FindWindow(None, window_name) # Find the window's hwnd for the first time
    if hwnd == 0:
        print(f"\"{window_name}\" is not currently open or does not exist.")
    else:
        print("Skipping ads.")
        while True:
            window_text = GetWindowText(hwnd) # Get the text of the window
            if not " - " in window_text and not window_name in window_text:
                SendMessage(hwnd, WM_CLOSE, 0, 0) # Close the application
                sleep(0.1)
                Popen(application_path) # Open the new window
                hwnd = FindWindow(None, window_name)  # Get hwnd tag of the newly opened window
                SetWindowPos(hwnd, HWND_BOTTOM, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE)  # Move window to the background
                sleep(1.5) # Give window time to set itself up
                press("playpause") # Start music
                print("Ad Skipped.")

            sleep(cycle_time)

if __name__ == "__main__":
    main()