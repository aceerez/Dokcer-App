import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog

import os
import ContainerClass
import ImagesClass

# initialize the tkinter GUI
root = tk.Tk()

root.geometry("1000x800")
root.pack_propagate(0)
root.resizable(0, 0)

bar_menu = Menu(root)
root.config(menu=bar_menu)

containerMenu = ContainerClass.Container(root)
imageMenu = ImagesClass.Images(root, containerMenu)


def InsertData():
    containerMenu.GetContainerList()
    imageMenu.GetImageList()


file_menu = Menu(bar_menu)
bar_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load Data", command=InsertData)
file_menu.add_command(label="New Docker File")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(bar_menu)
bar_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Delete All Containers")
edit_menu.add_command(label="Delete All Images")

root.mainloop()  # The mainloop for our tkinter Gui
