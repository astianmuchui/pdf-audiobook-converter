import tkinter
from tkinter import *
from tkinter import messagebox
import PyPDF2 as pyp
import pikepdf as pike
import pyttsx3 as pyt
import os
from os.path import isfile, join
from tkinter import filedialog


class AudConv():
    def __init__(self, parent):
        self.parent = parent
        self.buildWidgets()

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                   filetypes=(("Text files", "*.pdf*"), ("all files", "*.*")))

    def buildWidgets(self):
        self.voice_options = ["male", "female"]
        self.init_lbl = Label(self.parent, text="Upload A file ", bg="#fff", font=(12), fg="#bf2206")
        self.init_lbl.place(x=10, y=10)


if __name__ == "__main__":
    app = Tk()
    app.title("Audiobook Converter")
    app.geometry("700x500")
    app.configure(bg="#fff")
    root = AudConv(app)

    app.mainloop()
