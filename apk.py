from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import getpass
from PIL import ImageTk, Image 

# functions

def dwnload():
    try:
        if txtfld.get():
            link=txtfld.get()
            yt=YouTube(link)
            user=getpass.getuser()

            yd=yt.streams.get_highest_resolution()
            messagebox.showinfo("Downloading Status","Downloading, please wait")

            yd.download(r'C:\Users\{path}\Downloads\Youtube'.format(path=user))
            messagebox.showinfo("Downloading Status","Downloaded")
        else:
            messagebox.showinfo("Error occured!","Please paste YouTube link here")


    except:
        messagebox.showinfo("Downloading Status","Not a YouTube link")


import ctypes as ct


def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),ct.sizeof(value))


window=Tk()
window.geometry("600x400")
window.title("YouTube Video Downloader")
window.resizable(height=False, width=False)
dark_title_bar(window)


bg = ImageTk.PhotoImage(Image.open("G:\Codes\Python\Yt_video_downloader\img1.jpg"))
button_img = ImageTk.PhotoImage(Image.open("G:\Codes\Python\Yt_video_downloader\img2.png"))
icon_img = ImageTk.PhotoImage(Image.open("G:\Codes\Python\Yt_video_downloader\icon.ico"))

window.iconphoto(False, icon_img)


bg_panel = Label(window, image=bg)
bg_panel.pack(fill='both', expand='yes')

lgn_frame = Frame(window, width=400, height=200,highlightbackground="orange", highlightthickness=1)
lgn_frame.place(x=100, y=100)
lgn_frame.config(bg="#171717")

heading = Label(lgn_frame, text="PASTE YOUR LINK HERE", font=('yu gothic ui', 18, "bold"), fg='orange', bg="#171717", bd=5, relief=FLAT)
heading.place(x=50, y=30, width=300, height=30)

txtfld = Entry(lgn_frame, relief=FLAT, fg="orange",bg="#171717" ,font=("yu gothic ui ", 9), highlightthickness=2, highlightbackground="orange")
txtfld.place(x=72, y=75, width=258)

username_line = Canvas(lgn_frame, width=261, height=1.0, bg="orange",highlightthickness=0)
username_line.place(x=72, y=97, width=258)

lgn_button_label = Label(lgn_frame, image=button_img, bg="#171717")
lgn_button_label.place(x=150, y=140)
show_button = Button(lgn_frame,text='DOWNLOAD' ,command=dwnload, relief=FLAT,activebackground="#fa8507", borderwidth=0, bg="#fa8507", cursor="hand2", fg='black', font=("yu gothic ui", 9, "bold"), width=10, bd=0)
show_button.place(x=165, y=152)

window.mainloop()