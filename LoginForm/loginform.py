from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter.filedialog import *
from time import *
import json
import os


def register():
    try:
        file_path = "user_data.json"

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            data = {}

        user = username.get()
        pswd = password.get()
        up = False
        num = False
        up = any(char.isupper() for char in pswd)
        num = any(char.isnumeric() for char in pswd)

        if len(user) == 0 and len(pswd) == 0:
            messagebox.showerror("Error", "Please insert an username and a password first")
        elif len(user) == 0:
            messagebox.showerror("Error", "Please insert an username first")
        elif len(pswd) == 0:
            messagebox.showerror("Error", "Please insert a password first")
        elif user in data:
            messagebox.showerror("Error", "Choose another username")
        elif len(user) <=3:
            messagebox.showerror("Error","Your username must be at least 4 characters long")
        elif len(pswd) <=3:
            messagebox.showerror("Error","Your password must be at least 4 characters long")
        elif not num:
            messagebox.showerror("Error", "Your password should have at least one number")
        elif not up:
            messagebox.showerror("Error", "Your password should have at least one uppercase letter")
        else:
            data[user] = {
                'password': pswd,
                'time_string': strftime("%H:%M"),
                'day_string': strftime("%B %d, %Y")
            }

            username.delete(0, END)
            password.delete(0, END)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo("Registration", "Registered successfully")



    except FileNotFoundError:
        messagebox.showerror("Error", "No registered users found")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error reading user data")
    except Exception as e:
        print("An error has occured: ", e)

def see_pswd():
    try:
        if password.cget('show') == '*':
            password.config(show='')
            see.config(image=closed_eye)
        else:
            password.config(show='*')
            see.config(image=eye)
    except Exception as e:
        print("An error has occured: ", e)

def show_dashboard():
    file_path = "user_data.json"
    user = username.get()

    with open(file_path, 'r') as file:
        data = json.load(file)

    time_string = data[user]['time_string']
    day_string = data[user]['day_string']

    root.withdraw()
    dashboard = Toplevel(root)
    dashboard.title("User Dashboard")
    dashboard.geometry("400x300")
    dashboard.config(bg="#d4d1ee")
    dashboard.resizable(False,False)

    Label(dashboard,text="Welcome to your dashboard!", font=("Consolas", 14,"bold"),bg="#d4d1ee").pack(pady=20)
    Label(dashboard, text=f"Logged in as: {username.get()}", font=("Consolas", 12),bg="#d4d1ee").pack(pady=10)
    Label(dashboard,text=f"Account created on: {day_string}, {time_string}",font=("Consolas", 12),bg="#d4d1ee").pack(pady=10)

    Button(dashboard, text="Logout", font=("Consolas", 12), command=lambda: logout(dashboard),bg="#e5e3f4",activebackground="#e5e3f4").pack(pady=20)
    dashboard.protocol("WM_DELETE_WINDOW", lambda: logout(dashboard))
def logout(dashboard):
    dashboard.destroy()
    root.deiconify()

def login():
    file_path = "user_data.json"
    user = username.get()
    pswd = password.get()
    try:
        with open(file_path,'r') as file:
            data = json.load(file)

        if user in data:
            stored_pswd = data[user]['password']
            if pswd == stored_pswd:
                messagebox.showinfo("Login", "Login successful")
                show_dashboard()
            else:
                messagebox.showerror("Error", "Wrong password")
        else:
            messagebox.showerror("Error", "Username not found")
    except FileNotFoundError:
        messagebox.showerror("Error", "No registered users found")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error reading user data")
    except Exception as e:
        print("An error has occurred: ", e)



root = Tk()
root.title("Login Form")
root.geometry("500x200")
root.config(bg="#d4d1ee")
root.resizable(False,False)

eye = PhotoImage(file="C:\\Users\\sansf\\Desktop\\Programmazione\\Progetti Py\\LoginForm\\eye.png")
closed_eye = PhotoImage(file="C:\\Users\\sansf\\Desktop\\Programmazione\\Progetti Py\\LoginForm\\closed_eye.png")

frame = Frame(root)
frame.config(bg="#d4d1ee")
frame.pack()

Label(frame,text="Username: ",font=("Consolas",12),bg="#d4d1ee").grid(row=0,column=0,pady=(40,20))
username = Entry(frame,font=("Consolas",12),bg="#e5e3f4")
username.grid(row=0,column=1,pady=(40,20))

Label(frame,text="Password: ",font=("Consolas",12),bg="#d4d1ee").grid(row=1,column=0)
password = Entry(frame,font=("Consolas",12),show="*",bg="#e5e3f4")
password.grid(row=1,column=1)

see = Button(frame,image=eye,relief=FLAT,command=see_pswd,bg="#d4d1ee",activebackground="#d4d1ee")
see.grid(row=1,column=2)



login_button = Button(root, text="Login",font=("Consolas",12,"bold"),padx=10,command=login,bg="#e5e3f4",activebackground="#e5e3f4")
login_button.pack(side=RIGHT,padx=(0,150))

register_button = Button(root, text="Register",font=("Consolas",12,"bold"),padx=10,command=register,bg="#e5e3f4",activebackground="#e5e3f4")
register_button.pack(pady=20,side=LEFT,padx=(150,0))



root.mainloop()