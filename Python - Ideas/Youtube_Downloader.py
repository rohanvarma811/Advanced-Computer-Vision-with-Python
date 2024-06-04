from pytube import YouTube
import tkinter as tk

# 2-D Graphics Library
# Lets you use Graphical Interface
# Using here to have a directory Pop-up
# Visual Dialo Box to select where u want to save your File
from tkinter import filedialog

def download_video(url,save_path):
    try:
        # Take the instance of the Video
        yt= YouTube(url)
        # Streaming Quality of the video
        streams= yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream = streams.get_lowest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video Download Successful")

    except Exception as e:
        print(e)

# To make it User Friendly
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")

    return folder

if __name__ == "__main__":
    # Instantiate the TK module
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please Enter a Video Url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Downlaod...")
        download_video(video_url,save_dir)
    else:
        print("Invalid save Location!.")
