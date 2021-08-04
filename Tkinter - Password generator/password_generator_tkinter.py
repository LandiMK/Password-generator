# tkinter modules for GUI
    # tk -> tkinter module
    # Button -> tkinter Button
    # Entry -> tkinter text box
    # Label -> tkinter labels
    # StringVar -> Introduce special variables
    # messagebox -> tkinter message box notification
import tkinter as tk
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar
from tkinter import messagebox

# Modules for password creation
    # secrets -> Create cryptographical strong random numbers
    # string -> ASCII letters, numbers and punctuation
import secrets
import string

# Create variables for each type of character or data
alphabet = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

# Join all variables in one, to create a password
password_complete = alphabet + numbers + punctuation

# Initialized tkinter
window = tk.Tk()
# Window title
window.title("Password generator")
# Window size
window.geometry("250x150")

# User input
txt = Entry(window, width = 10)
# Text box position
txt.grid(column = 0, row = 2)
# Enter text writer automatically into the text box
txt.focus()

# Label
lbl = Label(window, text = "Password lenght")
lbl.grid(column = 0, row = 1)

# Function to generate the password with some conditions
def gen_psswd():
    '''Conditions to create the password'''

    number = txt.get()

    if (int(number) < 8):
        # Messagebox
        messagebox.showinfo("Error", "The password must have 8 characters!")

    elif (int(number) >= 8 and int(number) <= 30):
        # Join password's all parts
        password = "".join(secrets.choice(password_complete) for i in range (int(number)))

        # bd = 0 -> No border in text box
        entry = Entry(bd = 0)
        # (Position, text we want show)
        entry.insert(0, password)
        # entry.config(state = "readonly")
        # Where introduce our text box with X and Y positions
        entry.place(x=80, y=95, anchor="center")
        #entry.grid(column = 0, row = 4)

        # Label
            # f-string
        lbl_psswd = Label(window, text = f"Your password with {number} characters")
        lbl_psswd.place(x=95, y=70, anchor="center")

    else:
        # Messagebox
        messagebox.showinfo("Error", "The maximum lenght is 30!")

# Button
    # text -> Button text
    # bg -> Background color
    # fg -> Text color
    # command -> Button action when you click on it
btn = Button(window, text = "Generate", bg = "purple", fg = "white", command = gen_psswd)
btn.grid(column = 2, row = 2)

# Keep tkinter window active
window.mainloop()
