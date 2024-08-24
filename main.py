#Youtube Downloader
# Imports
import pytube
from tkinter import *
import customtkinter
import os
from tkinter import filedialog

#functions
def download(link):
    pass

def pathing():
    directory = filedialog.askdirectory()


root = customtkinter.CTk()
#variables
link = customtkinter.StringVar()
type = customtkinter.IntVar()
#1 = mp3
#2 = mp4

root.geometry("300x400")


#labels
title = customtkinter.CTkLabel(master=root, text="Youtube -> Mp3/Mp4", font=("TkDefaultFont", 20, 'bold'),fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)
download_label = customtkinter.CTkLabel(master=root, text="Download", fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)
video_link_label = customtkinter.CTkLabel(master=root, text="Video Link", fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)
file_name_label = customtkinter.CTkLabel(master=root, text="File Name", fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)

#user input
downloader = customtkinter.CTkButton(master=root, text="Download", command=download)
video_link = customtkinter.CTkEntry(master=root, placeholder_text="Video Link",placeholder_text_color="white", textvariable=link)
file_name = customtkinter.CTkEntry(master=root, placeholder_text="https://www.youtube.com/xxxxxxxxx", textvariable=link)
set_file_path = customtkinter.CTkButton(master=root, text="Set File Path", command=pathing)


optionmenu_var = customtkinter.StringVar(value="mp3")
optionmenu = customtkinter.CTkOptionMenu(master=root,values=["mp3", "mp4"], variable=optionmenu_var)

#place items
title.place(relx=0.5, rely=0.1, anchor=CENTER)
optionmenu.place(relx=0.5, rely=0.2, anchor=CENTER)
video_link_label.place(relx=0.5, rely=0.3, anchor=CENTER)
video_link.place(relx=0.5, rely=0.4, anchor=CENTER)
file_name_label.place(relx=0.5, rely=0.5, anchor=CENTER)
file_name.place(relx=0.5, rely=0.6, anchor=CENTER)
set_file_path.place(relx=0.5, rely=0.7, anchor=CENTER)
#download_label.place(relx=0.5, rely=0.7, anchor=CENTER)
downloader.place(relx=0.5, rely=0.9, anchor=CENTER)

#main program
root.mainloop()
