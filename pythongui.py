import tkinter as tk
from tkinter import filedialog, Text
import os
import invoke as inv
import ctypes
import pathlib


root = tk.Tk()
apps = []

#open the file dialog
#def bawb():

#    for widget in canvas.winfo_children():
#        widget.destroy()

#    filename = filedialog.askopenfilename(initialdir='/', title="bawb", filetypes=(("executables", "*.exe"), ("allfiles", "*.*")))
#    apps.append(filename)
#   print(filename)
#    for app in apps:
#        label = tk.Label( canvas, text=app, bg="grey")
#        label.pack()


canvas = tk.Canvas(root, height=700, width=700, bg="#272727")
canvas.pack()

calk = tk.Button(root, text="calk", fg="white", bg="#000000", command=bawb)
calk.pack()

root.mainloop()
