import webbrowser
from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.num_lock :
        webbrowser.open_new('https://zoro.to')
if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
