from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import sys
import signup
import main_app


# ---------------- RESOURCE PATH ----------------

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---------------- USER DETAILS ----------------

user_details = {}

def load_user_details():
    global user_details
    file_path = resource_path("user_details.txt")

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            user_details = eval(file.read())
    else:
        user_details = {}


# ---------------- LOGIN FUNCTION ----------------

def login_btn(username, password):
    load_user_details()

    if username != "" and password != "":
        if username == user_details.get("username") and password == user_details.get("password"):
            messagebox.showinfo("Login Successful", "Welcome to the Project")
            root.destroy()
            main_app.my_app_gui()
        else:
            messagebox.showerror("Login Failed", "Username and Password didn't match")
    else:
        messagebox.showwarning("Blank Detected", "Please fill all details")


def open_signup():
    root.destroy()
    signup.signup_page()


# ---------------- GUI ----------------

root = Tk() #WIN
root.geometry("1920x1080")
root.config(bg="dimgray")
root.title("Login")

img = Image.open(resource_path('image_logo.png'))
img=img.resize((200,200))
photoImg = ImageTk.PhotoImage(img)
login_label = Label(root,
                    compound=TOP,
                    text = "Login Here",
                    image=photoImg,
                    fg = 'black',
                    background='dimgray',
                    font = ("Arial",24,'bold'))
login_label.pack(pady=10)

user_row = Frame(root, bg = 'dimgray')
user_row.pack(pady = 30)

user_label = Label(user_row,
                   text = 'Username:',
                   fg='black',
                   bg='dimgray',
                   font=('Arial',16,'bold')
                   )
user_label.pack(side=LEFT, padx = 20)

user_frame = Frame(user_row, bg = "white")
user_frame.pack(side = LEFT, padx = 25)

user_entry = Entry(user_frame,
                   fg ='black',
                   bg = 'white',
                   bd = 0,
                   relief = SOLID,
                   show = "",
                   font = ('Arial',16,'bold'),
                   insertbackground='black')
user_entry.pack(side = LEFT, padx = 5, pady = 5)
user_entry.focus()

user_icon = ImageTk.PhotoImage(Image.open(resource_path("user_icon.png")).resize((25,25)))
def user():
    if pass_entry.cget("show") == "":
        eye_btn.config(image = user_icon)

user_btn = Button(user_frame, image = user_icon, bd = 0, fg = 'black', relief=SOLID, bg = 'white', activebackground='white')
user_btn.pack(side = RIGHT, padx = 5)

pass_row = Frame(root, bg = 'dimgray')
pass_row.pack(pady =30)

pass_label = Label(pass_row,
                   text = 'Password:',
                   fg='black',
                   bg='dimgray',
                   font=('Arial',16,'bold')
                   )
pass_label.pack(side=LEFT, padx = 25)

pass_frame = Frame(pass_row, bg = "white")
pass_frame.pack(side = LEFT, padx = 20)

pass_entry = Entry(pass_frame,
                   fg ='black',
                   bg = 'white',
                   bd = 0,
                   relief = SOLID,
                   show = "*",
                   font = ('Arial',16,'bold'),
                   insertbackground='black')
pass_entry.pack(side = LEFT, padx = 5, pady = 5)
pass_entry.focus()

eye_open = ImageTk.PhotoImage(Image.open(resource_path("open_eye.jpg")).resize((25,25)))
eye_close = ImageTk.PhotoImage(Image.open(resource_path("close_eye.png")).resize((25,25)))

def toggle_password():
    if pass_entry.cget("show") == "":
        pass_entry.config(show="*")
        eye_btn.config(image = eye_close)
    else:
        pass_entry.config(show = "")
        eye_btn.config(image = eye_open)

eye_btn = Button(pass_frame, image = eye_close, command = toggle_password, bd = 0, fg = 'black', relief=SOLID)
eye_btn.pack(side = RIGHT, padx = 5)

btn_frame = Frame(root, bg='dimgray')
btn_frame.pack(pady=20)

btn_login = Button(btn_frame,
                   text = 'Login',
                   command = lambda: login_btn(user_entry.get(), pass_entry.get()),
                   fg ='black',
                   bg = 'sky blue',
                   bd = 5,
                   relief = RAISED,
                   width = 10,
                   font = ('Arial',16,'bold'),
                   activeforeground='white',
                   activebackground='sky blue'
                   )
btn_login.pack(side = LEFT, padx = 35)

btn_signup = Button(btn_frame,
                   text ='Sign up',
                   command = open_signup,
                   fg ='black',
                   bg = 'blueviolet',
                   bd = 5,
                   relief = RAISED,
                   width = 10,
                   font = ('Arial',16,'bold'),
                   activebackground='blueviolet',
                   activeforeground='white'
                   )
btn_signup.pack()
root.mainloop()
