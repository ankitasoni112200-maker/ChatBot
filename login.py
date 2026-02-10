from tkinter import * #GUI
from PIL import Image, ImageTk
import signup
from tkinter import messagebox
import os
import main_app

user_details = {}
def load_user_details():
    global user_details
    if os.path.exists("./user_details.txt"):
        file = open('./user_details.txt', 'r')
        user_details = eval(file.read())
        print(user_details)
        #print(type(user_details))
        file.close()
    else:
        print("no file found to login")


def login_btn(username, password):
    global user_details
    if username !="" and password != "":
        if user_details == {}:
            load_user_details()
        if username == user_details['username'] and password == user_details['password']:
             messagebox.showinfo("Login Successful", "Welcome to the Project")
             root.destroy()
             main_app.my_app_gui() # chatbot screen
        else:
            messagebox.showerror("Login failed", "username and password didn't match")

    else:
        messagebox.showwarning("Blank detected", "Kindly fill all the details")

def open_signup():
    root.destroy()
    signup.signup_page()



root = Tk() #WIN
root.geometry("1920x1080")
root.config(bg="dimgray")
root.title("Login")

img = Image.open('image_logo.png')
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

user_icon = ImageTk.PhotoImage(Image.open("user_icon.png").resize((25,25)))

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

eye_open = ImageTk.PhotoImage(Image.open("open_eye.jpg").resize((25,25)))
eye_close = ImageTk.PhotoImage(Image.open("close_eye.png").resize((25,25)))

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