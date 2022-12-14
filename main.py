from pynput import keyboard

text_history = []

def processKeys(key : keyboard.Key):
    global text_history

    if key == keyboard.Key.backspace:
        if len(text_history) > 0:
            text_history.pop(len(text_history) - 1)
    elif key == keyboard.Key.enter:
        text_history.clear()
    elif key == keyboard.Key.shift or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
        pass
    elif key == keyboard.Key.tab:
        text_history.append("   ")
    elif key == keyboard.Key.space:
        text_history.append(" ")

def get_key_string(key : keyboard.Key | keyboard.KeyCode | None):
    if isinstance(key, keyboard.Key):
        return key

def on_press(key : keyboard.Key | keyboard.KeyCode | None):
    if isinstance(key, keyboard.Key):
        processKeys(key)
    if isinstance(key, keyboard.KeyCode):
        text_history.append(key.char)
    print("".join(text_history))

if __name__ == "__main__" :
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()