from hashlib import sha256
from tkinter import *
import pyperclip
import pyautogui

FONT_TITLE = ('JetBrains mono', 14, 'bold')
FONT_HASH = ('JetBrains mono', 11, 'bold')


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

    if e.char == '\x15':
        pwd_input.delete(0, 'end')
        hash_label.config(text='H4SH3D P4SSW0RD')

    if e.char == '\x0e':
        pwd_input.config(show='*')

    if e.char == '\x13':
        pwd_input.config(show='')


window = Tk()
window.minsize(width=650, height=100)
window.resizable(0, 0)
window.title('Hash password')
window.config(pady=50, bg='white')
window.eval('tk::PlaceWindow . center')

Label(text='ENTER THE PASSWORD', pady=15, bg='white', font=FONT_TITLE).pack()

pwd_input = Entry(width=40)
pwd_input.config(justify='center', show='*', font=FONT_HASH, borderwidth=0)
pwd_input.focus()
pwd_input.pack()

hash_label = Label(text='H4SH3D P4SSW0RD')
hash_label.config(pady=30, fg='#006400', bg='white',
                  font=FONT_HASH)
hash_label.pack()

window.bind('<KeyPress>', get_hash)
window.lift()
window.attributes('-topmost', True)

window.mainloop()
