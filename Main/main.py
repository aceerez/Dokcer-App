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
root.resizable (0, 0)

containerMenu = ContainerClass.Container(root)
imageMenu = ImagesClass.Images(root)



root.mainloop ()  # The mainloop for our tkinter Gui
