import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog
import pandas as pd
import os
import  ContainerClass
import ImagesClass
# initialize the tkinter GUI
root = tk.Tk ()

root.geometry ("1000x800")
root.pack_propagate (0)
root.resizable(0, 0)

bar_menu=Menu(root)
root.config(menu=bar_menu)

containerMenu = ContainerClass.Container(root)
imageMenu = ImagesClass.Images(root)

file_menu = Menu(bar_menu)
bar_menu.add_cascade(label="Actions", menu=file_menu)
file_menu.add_command(label="Load Container List",command=containerMenu.GetContainerList)
file_menu.add_command(label="Load Image List",command=imageMenu.GetImageList)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop ()  # The mainloop for our tkinter Gui
 
