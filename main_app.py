from tkinter import *
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk
import webbrowser
import pandas as pd
import pywhatkit
import voice_recognition
import speech_output
import sys

# ---------------- RESOURCE PATH (EXE SAFE) ----------------

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------- FILE PATHS ----------------

FILE_NAME = resource_path("chatbot_data.txt")

webbrowser_list = ['google', 'youtube', 'facebook', 'google maps']

# ---------------- LOAD DATA ----------------

def load_data():
    data = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding="utf-8") as file:
            for line in file:
                if "|" in line:
                    q, a = line.strip().split('|', 1)
                    data[q.lower()] = a
    return data

# ---------------- SAVE DATA ----------------

def save_data(q, a):
    with open(FILE_NAME, 'a', encoding="utf-8") as file:
        file.write(f"\n{q}|{a}")

# ---------------- IMPORT FILE ----------------

def import_data_file():
    global data
    file_path = filedialog.askopenfilename(
        title="Select Data File",
        filetypes=(("CSV Files", "*.csv"), ("Text Files", "*.txt"))
    )

    if not file_path:
        return

    try:
        count = 0
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            for _, row in df.iterrows():
                q, a = str(row[0]).strip(), str(row[1]).strip()
                if q and a:
                    data[q.lower()] = a
                    save_data(q, a)
                    count += 1
        else:
            with open(file_path, 'r') as file:
                for line in file:
                    if '|' in line:
                        q, a = line.strip().split('|', 1)
                        data[q.lower()] = a
                        save_data(q, a)
                        count += 1

        messagebox.showinfo("✅ Success", f"Imported {count} Q&A pairs from:\n{file_path}")
    except Exception as e:
        messagebox.showerror("❌ Error", f"Failed to import data:\n{e}")

# ---------------- TEACH BOT ----------------

def teach_bot(question):
    def save_answer():
        ans = ans_entry.get().strip()
        if ans != "":
            data[question.lower()] = ans
            save_data(question, ans)
            chat.insert(END, f"Bot learned: {ans}\n")
            speech_output.speak_text(f"I learned: {ans}")
            for url_name in webbrowser_list:
                if url_name in user_msg.lower():
                    webbrowser.open(f"www.{url_name}.com")
            train_win.destroy()

    train_win = Toplevel(new_win)
    Label(train_win, text=f"Answer for '{question}'").pack(pady=5)

    ans_entry = Entry(train_win, width=40)
    ans_entry.pack(pady=5)

    Button(train_win, text='Save', command=save_answer).pack(pady=5)

def send():
    global user_msg
    user_msg = chat_entry.get().strip()

    if not user_msg:
        return

    chat.insert(END, f"You: {user_msg}\n")

    global data
    if "play" in user_msg.lower() and "youtube" in user_msg.lower():
        try:
            song_name = user_msg.lower().replace('play', '').replace('on youtube', "").strip()
            if song_name:
                chat.insert(END, f"Bot: Playing {song_name}")
                speech_output.speak_text(f"Playing {song_name} on Youtube")
                pywhatkit.playonyt(song_name)
            else:
                chat.insert(END, f"Bot: Please tell me which song you want to play on youtube")
                speech_output.speak_text(f"Please tell me which song you want to play on Youtube")
        except Exception as e:
            speech_output.speak_text(f"Sorry i didn't get you")
            print(e)

    elif "search" in user_msg.lower() and "google" in user_msg.lower():
        try:
            search_data = user_msg.lower().replace('search', '').replace('on google', "").strip()
            if search_data:
                chat.insert(END, f"Bot: Searching {search_data}")
                speech_output.speak_text(f"Searching {search_data} on google")
                pywhatkit.search(search_data)
            else:
                chat.insert(END, f"Bot: Please tell me what do you want to search on google")
                speech_output.speak_text(f"Please tell me what do you want to search on google")
        except Exception as e:
            speech_output.speak_text(f"Sorry I didn't get you.")
            print(e)

    elif "search" in user_msg.lower() and "google maps" in user_msg.lower():
        try:
            location = user_msg.lower().replace('search', '').replace('on google maps', "").strip()
            if location:
                chat.insert(END, f"Bot: Searching {location}")
                speech_output.speak_text(f"Searching {location} on google maps")
                pywhatkit.search(location)
            else:
                chat.insert(END, f"Bot: Please tell me which location do you want to search on google maps")
                speech_output.speak_text(f"Please tell me which location do you want to search on google maps")
        except Exception as e:
            speech_output.speak_text(f"Sorry I didn't get you.")
            print(e)

    elif user_msg.lower() in data:
        reply = data[user_msg.lower()]
        chat.insert(END, f"Bot: {reply}\n")

        speech_output.speak_text(reply)

        for url_name in webbrowser_list:
            if url_name in user_msg.lower():
                webbrowser.open(f"www.{url_name}.com")
    else:
        chat.insert(END, "Bot: I don't know that. Please teach me!\n")
        speech_output.speak_text("I don't know that. Please teach me!")

        teach_bot(user_msg)

    chat_entry.delete(0, END)

# ---------------- MAIN GUI ----------------

def my_app_gui():
    global chat_entry, chat, new_win

    new_win = Tk()
    new_win.title('Chatbot')
    new_win.geometry("1920x1080")
    new_win.config(bg='dimgray')

    chat_bot_img = Image.open(resource_path('chatbot.3D.webp'))
    chat_bot_img = chat_bot_img.resize((200, 200))
    final_image = ImageTk.PhotoImage(image=chat_bot_img)
    chat_label = Label(
        new_win,
        image=final_image,
        text="ChatBot",
        compound=LEFT,
        font=('Times New Roman', 24, 'bold'),
        fg="whitesmoke",
        bg='dimgray'
    )
    chat_label.pack()

    chat_frame = Frame(new_win, width=80, bg='lightgray')
    chat_frame.pack()

    chat = Text(chat_frame, width=80, height=15,
                font=('Arial', 15, 'bold'), fg="black", bg='whitesmoke')
    chat.pack(pady=20)

    chat_entry = Entry(chat_frame, width=40, font=('Arial', 13, 'bold'), fg='black',bg='whitesmoke')
    chat_entry.pack(side=LEFT, padx=5)

    # --- Send Button ---
    btn_send = Button(chat_frame, text='Send', command=send,
                      font=("Times New Roman", 13, 'bold'),
                      width=10, fg="black", bg='mediumpurple')
    btn_send.pack(side=LEFT, padx = 5, pady = 5)

    def voice_input():
        voice_text = voice_recognition.recognize_voice()
        if voice_input:
            chat_entry.delete(0,END)
            chat_entry.insert(0, voice_text)
            send()
    
    btn_voice = Button(chat_frame, text='MIC', command=voice_input, font=("Times New Roman", 13, 'bold'),
                        width=10, fg="black", bg='mediumorchid')
    btn_voice.pack(side=LEFT, padx=5, pady = 5)

    # --- Upload Data Button ---
    btn_upload = Button(chat_frame, text='Upload Data',
                        command=import_data_file,
                        font=("Times New Roman", 13, 'bold'),
                        width=10, fg="black", bg='plum')
    btn_upload.pack(side=LEFT, padx=5, pady = 5)


    chat.insert(END, "Bot: Hello! Ask me something!!!\n")
    speech_output.speak_text("Hello ask me something")

    new_win.mainloop()


# --- Load data once at startup ---
data = load_data()

# Uncomment for direct test without login
#my_app_gui()
