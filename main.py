#Youtube Downloader
# Imports
import tkinter.messagebox
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
from tkinter import *
import customtkinter
from tkinter import filedialog
import tkinter

directory = ""
#functions
def download():
    global root
    global link
    global directory
    global optionmenu_var
    global filename_var
    
    #check if options are valid
    if filename_var.get() == "" or directory == "":
        box = tkinter.messagebox.showinfo(master=root, message="Please make sure to enter a valid video link, a file name and select a directory!")
    else:
       # try:
            #check download type
            if optionmenu_var.get() == "mp3":
                yt = YouTube(link.get(), on_progress_callback=on_progress)
                video = yt.streams.filter(only_audio=True).first()
                video.download(output_path=directory, filename=str(filename_var.get() + ".mp3"))
            elif optionmenu_var.get() == "mp4":
                yt = YouTube(link.get(), on_progress_callback=on_progress)
                #video = yt.streams.filter(progressive=True).get_by_resolution(str(resolution_var.get()))
                video = yt.streams.filter().first()

                video.download(output_path=directory, filename=str(filename_var.get() + ".mp4")) 
            #playlist downloads
            elif optionmenu_var.get() == "mp3 (playlist)":
                p = Playlist(link.get())
                for video in p.videos:
                    video.streams.filter(only_audio=True).first().download(output_path=directory, filename=str(filename_var.get() + " - " + video.title + ".mp3"))
            elif optionmenu_var.get() == "mp4 (playlist)":
                p = Playlist(link.get())
                for video in p.videos:
                    #printing for debugging
                    print(video)
                    video.streams.filter().first().download(output_path=directory, filename=str(filename_var.get() + " - " + video.title + ".mp4"))
        #except:
          #  box = tkinter.messagebox.showinfo(master=root, message="Please make sure to enter a valid video link, a file name and select a directory!")

#get path
def pathing():
    global directory
    directory = filedialog.askdirectory()

#main
root = customtkinter.CTk()
#variables
link = customtkinter.StringVar()
type = customtkinter.IntVar()
filename_var = customtkinter.StringVar()
filename_var.set("")
#1 = mp3
#2 = mp4

#window settings
root.geometry("300x400")
root.resizable(False, False)
root.title("Youtube -> Downloader")

#labels
title = customtkinter.CTkLabel(master=root, text="Youtube -> Mp3/Mp4", font=("TkDefaultFont", 20, 'bold'),fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)
download_label = customtkinter.CTkLabel(master=root, text="Download", fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)
video_link_label = customtkinter.CTkLabel(master=root, text="Video Link", fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)
file_name_label = customtkinter.CTkLabel(master=root, text="File Name", fg_color="#1b79f5", padx=5, pady=5, corner_radius=5)

#user input
downloader = customtkinter.CTkButton(master=root, text="Download", command=download)
video_link = customtkinter.CTkEntry(master=root, placeholder_text="Video Link",placeholder_text_color="white", textvariable=link)
file_name = customtkinter.CTkEntry(master=root, placeholder_text="https://www.youtube.com/xxxxxxxxx", textvariable=filename_var)
set_file_path = customtkinter.CTkButton(master=root, text="Set File Path", command=pathing)


#options
optionmenu_var = customtkinter.StringVar(value="mp3")
optionmenu = customtkinter.CTkOptionMenu(master=root,values=["mp3", "mp4", "mp3 (playlist)","mp4 (playlist)"], variable=optionmenu_var)

#resolution
resolution_var = customtkinter.StringVar(value="720p")
resolutionmenu = customtkinter.CTkOptionMenu(master=root,values=["144p", "240p", "360p","480p", "720p"], variable=resolution_var)

#place items
title.place(relx=0.5, rely=0.1, anchor=CENTER)
optionmenu.place(relx=0.5, rely=0.2, anchor=CENTER)
#link
video_link_label.place(relx=0.5, rely=0.3, anchor=CENTER)
video_link.place(relx=0.5, rely=0.4, anchor=CENTER)
#file
file_name_label.place(relx=0.5, rely=0.5, anchor=CENTER)
file_name.place(relx=0.5, rely=0.6, anchor=CENTER)
#resolution
resolutionmenu.place(relx=0.5, rely=0.7, anchor=CENTER)
set_file_path.place(relx=0.5, rely=0.8, anchor=CENTER)
#download_label.place(relx=0.5, rely=0.7, anchor=CENTER)
downloader.place(relx=0.5, rely=0.9, anchor=CENTER)


#main program
root.mainloop()