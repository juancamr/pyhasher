from hashlib import sha256
from tkinter import Tk, Label, Entry
import pyperclip
import pyautogui


class Pyhasher:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(width=650, height=100)
        self.window.resizable(False, False)
        self.window.title("Hash password")
        self.window.config(pady=50, bg="black")
        self.window.eval("tk::PlaceWindow . center")

        Label(
            text="ENTER THE PASSWORD",
            pady=15,
            bg="black",
            fg="white",
            font=("Cascadia Code", 14, "bold"),
        ).pack()

        self.pwd_input = Entry(width=40)
        self.pwd_input.config(
            justify="center",
            show="*",
            font=("Cascadia Code", 11, "bold"),
            borderwidth=0,
            bg="black",
            fg="white",
        )
        self.pwd_input.focus()
        self.pwd_input.pack()

        self.hash_label = Label(text="H4SH3D P4SSW0RD")
        self.hash_label.config(
            pady=30, fg="#006400", bg="black", font=("Cascadia Code", 11, "bold")
        )
        self.hash_label.pack()

        self.window.bind("<KeyPress>", self.get_hash)
        self.window.lift()
        self.window.attributes("-topmost", True)

    def get_hash(self, e):
        hash_password = sha256(self.pwd_input.get().encode("utf-8")).hexdigest()
        self.hash_label.config(text=hash_password.upper())

        if self.pwd_input.get() == "":
            self.hash_label.config(text="H4SH3D P4SSW0RD")

        if e.char == "\r":
            pyperclip.copy(hash_password)
            self.window.destroy()
            with pyautogui.hold("ctrl"):
                pyautogui.press(["v"])

        if e.char == "\x15":
            self.pwd_input.delete(0, "end")
            self.hash_label.config(text="H4SH3D P4SSW0RD")

        if e.char == "\x0e":
            self.pwd_input.config(show="*")

        if e.char == "\x13":
            self.pwd_input.config(show="")

        if e.char == "\x03":
            self.window.destroy()

    def run(self):
        self.window.mainloop()


pyhasher = Pyhasher()
pyhasher.run()
