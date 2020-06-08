#!/usr/bin/python3

from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
from tkinter import filedialog

def download():
    output_folder = tk.filedialog.askdirectory()
    url = ent_url.get()
    ydl_opts = {
    'outtmpl': output_folder + '/%(title)s.%(ext)s',
    'restrictfilenames': True,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    lbl_output['text'] = 'Success! Downloaded to {}'.format(output_folder)
    ent_url.delete(0, tk.END)

# Window

window = tk.Tk()
window.title('Youtube Downloader')

frm_entry = tk.Frame(master=window)
lbl_url = tk.Label(master=frm_entry, text='Enter URL Here')
ent_url = tk.Entry(master=frm_entry, width = 40)

lbl_url.grid(row=0, column=0)
ent_url.grid(row=0, column=1)

btn_convert = tk.Button(
    master=window,
    text='Convert!',
    command=download)

lbl_output = tk.Label(master=window, text='Nothing converted yet.')

frm_entry.grid(row=0, column=0, pady=10, padx=10)
btn_convert.grid(row=1, column=0, pady=10)
lbl_output.grid(row=2, column=0, pady=10)

window.mainloop()