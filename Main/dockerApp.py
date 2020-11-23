#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from tkinter import filedialog, simpledialog

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


def DeleteAllContainers():
    containerMenu.DeleteAllContainer()


def DeleteAllImages():
    imageMenu.DeleteAllImage()


def NewDockerFile():
    answer = simpledialog.askstring("Docker File Name", "Enter Docker file name ")
    os.system('gnome-terminal -- bash -c "nano ./dockerFiles/{0}; exec bash"'.format(answer))


def EditDOckerFile():
    path = filedialog.askopenfilename(initialdir="./dockerFiles",
                                      title="Select Only A Docker File")
    print(path)
    if not path:
        return
    else:
        os.system('gnome-terminal -- bash -c "nano {0}; exec bash"'.format(path))


file_menu = Menu(bar_menu)
bar_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load Data", command=InsertData)
file_menu.add_separator()
file_menu.add_command(label="New Docker File", command=NewDockerFile)
file_menu.add_command(label="Edit Docker File", command=EditDOckerFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(bar_menu)
bar_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Delete All Containers", command=DeleteAllContainers)
edit_menu.add_command(label="Delete All Images", command=DeleteAllImages)

loadbtn = Button(root, text="Load Docker \n Data", command=InsertData, font=("arial", 30))
loadbtn.place(rely=0.4, relx=0)
root.mainloop()  # The mainloop for our tkinter Gui
