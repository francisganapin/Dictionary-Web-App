import keyboard
import pyautogui

def scroll_up():
    pyautogui.scroll(10)  # Scroll up

def scroll_down():
    pyautogui.scroll(-10)  # Scroll down

keyboard.add_hotkey('8', scroll_up)
keyboard.add_hotkey('2', scroll_down)

print("Press '8' to scroll up and '2' to scroll down. Press 'esc' to exit.")

keyboard.wait('/')  # Wait for the 'esc' key to exit
