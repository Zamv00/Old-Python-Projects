from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import time
import string
import random

def password():
    #password gen function
    try:
        length = int(passlength.get(1.0, END))

        if length <= 0 or length > 30:
            messagebox.showerror("Too Long", "Please insert a length between 1 and 30.\nPress OK to continue")
            passlength.delete(1.0, END).strip()

            return

    except ValueError:
        messagebox.showerror("Invalid Input", "Please insert a valid number")
        passlength.delete(1.0, END)
        return

    exclude_symbols = '+-;<=>[]^_`{|}`()"\','
    custom_punctuation = ''.join(char for char in string.punctuation if char not in exclude_symbols)
    characters = '' #intialize characters as an empty string and adds letters, numbers or symbols based on the value of the variables x, y and z
    if x.get() == 1:
        characters += string.ascii_letters
    if y.get() == 1:
        characters += string.digits
    if z.get() == 1:
        characters += custom_punctuation
    if not characters: #in python an empty string evalutes to False, so 'not characters' will be True if characters is equal to ''
        messagebox.showerror("No Character Types Selected",
                            "Please select at least one checkbox.\nPress OK to continue")

        return

    pswd_list = random.choices(characters, k=length)
    pswd = ''.join(pswd_list)
    final_pass.config(state=NORMAL)
    final_pass.delete(1.0,END)
    final_pass.insert(1.0, pswd)
    root.update()
    final_pass.config(state=DISABLED)




#Creating the root
root = Tk()
root.geometry("300x200")
root.resizable(False,False)
root.configure(bg="#2F3C7E")


x= IntVar(value=1)
y = IntVar(value=1)
z = IntVar(value=1)


#frame to hold buttons
frame = Frame(root,pady=10)
frame.pack()
frame.configure(bg="#2F3C7E")
Label(frame, text="Insert password length: " , font=("Consolas", 10), bg="#FBEAEB").grid(row=0, column=0, padx=5)
passlength = Text(frame, width=3, height=1, bg="#FBEAEB", font=("Consolas", 12))
passlength.grid(row=0,column=1)

#generate password button
gen_password = Button(command=password, text="Generate Password", font=("Consolas", 10), bg="#FBEAEB")
gen_password.pack()

#the generated password
final_pass = Text(width=30, height=1, state = DISABLED, bg="#FBEAEB", font=("Consolas", 12))
final_pass.pack(side=TOP, pady=10)


letters_check = Checkbutton(text="A-Z",
                            variable=x,
                            offvalue=0,
                            bg="#FBEAEB")
letters_check.pack()

numbers_check = Checkbutton(text="0-9",
                            variable=y,
                            offvalue=0,
                            bg="#FBEAEB")
numbers_check.pack()

simbols_check = Checkbutton(text= "!@#$%^&",
                            variable=z,
                            offvalue=0,
                            bg="#FBEAEB")
simbols_check.pack()




root.mainloop()