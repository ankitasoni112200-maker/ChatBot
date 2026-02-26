from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import sys


# ---------------- RESOURCE PATH ----------------

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def register_details(username, password, mobile, email):

    if username and password and mobile and email:

        data = {
            "username": username,
            "password": password,
            "mobile": mobile,
            "email": email
        }

        file_path = resource_path("user_details.txt")

        with open(file_path, "w") as file:
            file.write(str(data))

        messagebox.showinfo("Success", "Registration Successful")
        signup_root.destroy()

    else:
        messagebox.showerror("Error", "Fill all details")

def signup_page():
    global signup_root
    signup_root = Tk()
    signup_root.geometry("1920x1080")
    signup_root.config(bg="black")
    signup_root.title("Sign Up Page")

    main_frame = Frame(signup_root, bg="black")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    img = Image.open(resource_path('signup_image.png'))
    img=img.resize((160,160))
    photoImg = ImageTk.PhotoImage(img)
    signup_label = Label(signup_root,
                    compound=TOP,
                    text = "Sign up",
                    image=photoImg,
                    fg = 'white',
                    background='black',
                    font = ("Arial",20,'bold'))
    signup_label.pack()

    user_frame = Frame(signup_root, bg = 'black')
    user_frame.pack(pady = 20)

    user_label = Label(user_frame,
                   text = 'Username',
                   fg='white',
                   bg='black',
                   font=('Arial',16,'bold'),
                   anchor = 'e')
    user_label.pack(side=LEFT, padx=25)

    user_entry = Entry(user_frame,
                   fg ='white',
                   bg = 'black',
                   bd = 5,
                   relief = RAISED,
                   font = ('Arial',16,'bold'),
                   insertbackground='white',
    )
    user_entry.pack()
    user_entry.focus()

    pass_frame = Frame(signup_root, bg = 'black')
    pass_frame.pack(pady = 20)

    pass_label = Label(pass_frame,
                   text = 'Password',
                   fg='white',
                   bg='black',
                   font=('Arial',16,'bold'),
                   anchor = 'e'
                   )
    pass_label.pack(side=LEFT, padx=25)

    pass_entry = Entry(pass_frame,
                   fg ='white',
                   bg = 'black',
                   bd = 5,
                   relief = RAISED,
                   font = ('Arial',16,'bold'),
                   insertbackground='white')
    pass_entry.pack()
    pass_entry.focus()

    mobilenumber_frame = Frame(signup_root, bg = 'black')
    mobilenumber_frame.pack(pady = 20, padx= 20)

    mobilenumber_label = Label(mobilenumber_frame,
                   text = 'Mobile Number',
                   fg='white',
                   bg='black',
                   font=('Arial',16,'bold'),
                   anchor = 'e'
                   )
    mobilenumber_label.pack(side=LEFT, padx=20)

    mobilenumber_entry = Entry(mobilenumber_frame,
                   fg ='white',
                   bg = 'black',
                   bd = 5,
                   relief = RAISED,
                   font = ('Arial',16,'bold'),
                   insertbackground='white')
    mobilenumber_entry.pack()
    mobilenumber_entry.focus()

    email_frame = Frame(signup_root, bg = 'black')
    email_frame.pack(pady = 15)

    email_label = Label(email_frame,
                   text = 'Email',
                   fg='white',
                   bg='black',
                   font=('Arial',16,'bold'),
                   anchor = 'e'
                   )
    email_label.pack(side=LEFT, padx=45)

    email_entry = Entry(email_frame,
                   fg ='white',
                   bg = 'black',
                   bd = 5,
                   relief = RAISED,
                   font = ('Arial',16,'bold'),
                   insertbackground='white')
    email_entry.pack()
    email_entry.focus()

    btn_frame = Frame(signup_root, bg='black')
    btn_frame.pack(pady=20)

    register_btn = Button(btn_frame,
                      text= 'Register',
                      command = lambda:register_details(user_entry.get(),pass_entry.get(),mobilenumber_entry.get(),email_entry.get()),
                      fg ='white',
                      bg = 'blueviolet',
                      bd = 5,
                      relief = RAISED,
                      width = 10,
                      font = ('Arial',16,'bold'),
                      activeforeground='white',
                      activebackground='blueviolet')
    register_btn.pack(side = LEFT, padx = 20)

    signup_root.mainloop()
