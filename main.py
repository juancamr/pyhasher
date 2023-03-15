import pyperclip
import pyautogui
from hashlib import sha256
from tkinter import *


def get_hash(e):
    hash_password = sha256(pwd_input.get().encode('utf-8')).hexdigest()
    hash_label.config(text=hash_password.upper())

    if pwd_input.get() == '':
        hash_label.config(text='H4SH3D P4SSW0RD')

    if e.char == "\r":
        pyperclip.copy(hash_password)
        window.destroy()
        with pyautogui.hold('ctrl'):
            pyautogui.press(['v'])


window = Tk()
window.minsize(width=600, height=100)
window.title('Hash password')
window.config(pady=50)
window.eval('tk::PlaceWindow . center')
window.configure(bg='black')

Label(text='ENTER THE PASSWORD', bg='black', fg='white', pady=15).pack()

pwd_input = Entry(width=30)
pwd_input.config(bg='black', insertbackground='white', fg='white', justify='center')
pwd_input.focus()
pwd_input.pack()

hash_label = Label(text='H4SH3D P4SSW0RD')
hash_label.config(pady=30, bg='black', fg='#39FF14')
hash_label.pack()

window.bind('<KeyPress>', get_hash)
window.lift()
window.attributes('-topmost', True)
window.mainloop()
