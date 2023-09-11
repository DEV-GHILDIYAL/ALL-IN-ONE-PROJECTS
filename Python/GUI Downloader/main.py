import tkinter  as tk
from tkinter import ttk, filedialog
import requests

class Downloader:
    def __init__(self):
        self.saveTo = ""
        self.window = tk.Tk()
        self.window.title("Downloader")
        self.url_label = tk.Label(text="Enter URL").pack()
        self.url_entry = tk.Entry().pack()
        self.browse_button = tk.Button(text="Browse",  command=self.browse_file).pack()
        self.download_button = tk.Button(text="Download",  command=self.download_file).pack()
        self.window.geometry("844x344")
        self.window.config(bg="blue")
        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=300, mode="determinate").pack()
        self.window.mainloop()
    
    def browse_file(self):
        saveTo = filedialog.asksaveasfile()
        self.url_entry.saveTo =  saveTo

    def download_file(self):
        url = self.url_entry.get()
        response = requests.get(url)
        total_size_in_bytes = response.headers.get("content-length")
        block_size = 10000
        self.progress_bar["value"] = 0
        fileName = self.url_entry.get().split("/")[-1]
        with open(fileName, "wb") as f:
            for data in response.iter_content(block_size):
                self.progress_bar["value"] = (100*block_size)/total_size_in_bytes
                self.window.update()
                f.write(data)

Downloader()