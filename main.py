import history
import traceback

from pynput import keyboard
from lib.alert import do_alert
from lib.error import EndsWithInvalidWordException

def processKeys(key : keyboard.Key):
    if key == keyboard.Key.backspace:
        if not history.is_empty():
            history.pop_right()
    elif key == keyboard.Key.enter:
        history.validate()
        history.clear()
    elif key == keyboard.Key.tab:
        history.append("   ")
    elif key == keyboard.Key.space:
        history.append(" ")

def get_key_string(key : keyboard.Key | keyboard.KeyCode | None):
    if isinstance(key, keyboard.Key):
        return key

def on_press(key : keyboard.Key | keyboard.KeyCode | None):
    if isinstance(key, keyboard.Key):
        try:
            processKeys(key)
        except EndsWithInvalidWordException as e :
            do_alert()
        except Exception as e:
            traceback.print_exc()
    if isinstance(key, keyboard.KeyCode):
        history.append(key.char)
    print("".join(history.to_list()))

if __name__ == "__main__" :
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()