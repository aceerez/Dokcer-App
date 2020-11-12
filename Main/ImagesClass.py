import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog
import pandas as pd
import os
import ContainerClass


class Images:
    def __init__(self, master):

        # This is the frame for the Images Treeview
        self.imagTreeFrame = tk.LabelFrame (master, text="Images list")
        self.imagTreeFrame.place (height=250, width=600, rely=0.6, relx=0.0)

        # This is the frame for the info for Images and its action
        self.imagInfoFrame = tk.LabelFrame (master, text="Images INFO")
        self.imagInfoFrame.place (height=75, width=400, rely=.48, relx=0)

        self.imagInfoLbl = ttk.Label (self.imagInfoFrame, text="Press to Load Images List")
        self.imagInfoLbl.place (rely=0, relx=0)
        self.imagLodlistBtn = tk.Button (self.imagInfoFrame, text="Load Images List",
                                         command=lambda: self.GetImageList ())
        self.imagLodlistBtn.place (rely=0.5, relx=0)
        ##doker hub credentials
        self.hubFrame = tk.LabelFrame (master, text="Enter your Docker Hub credentials ")
        self.hubFrame.place (height=150, width=250, rely=0.37, relx=0.64)

        self.hubUserNamelbl = tk.Label (self.hubFrame, text="User Name")
        self.hubUserNamelbl.place (rely=0.2, relx=0.1)
        self.hubPasswordlbl = tk.Label (self.hubFrame, text="PassWord")
        self.hubPasswordlbl.place (rely=0.5, relx=0.1)
        self.hubUserNameEntry = tk.Entry()
        self.hubUserNameEntry.place (rely=0.425, relx=0.76)
        self.hubUserPassWordEntry = tk.Entry ()
        self.hubUserPassWordEntry.place (rely=0.475, relx=0.76)
        # craete Image tree View

        self.imagTreViw = ttk.Treeview (self.imagTreeFrame)  # This is the Treeview Widget
        column_list_account = ["Image ID"]  # These are our headings
        self.imagTreViw ['columns'] = column_list_account  # We assign the column list to the widgets columns
        self.imagTreViw ["show"] = "headings"  # this hides the default column..

        for column in column_list_account:  # foreach column
            self.imagTreViw.heading (column, text=column)  # let the column heading = column name
            self.imagTreViw.column (column, width=50)  # set the columns size to 50px

        self.imagTreViw.place (relheight=1,
                               relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).
        self.imagtreescroll = tk.Scrollbar (self.imagTreeFrame)  # create a scrollbar
        self.imagtreescroll.configure (command=self.imagTreViw.yview)  # make it vertical
        self.imagTreViw.configure (
            yscrollcommand=self.imagtreescroll.set)  # assign the scrollbar to the Treeview Widget
        self.imagtreescroll.pack (side="right", fill="y")  # make the scrollbar fill the yaxis of the Treeview widget

        self.imagPopMenu = Menu (master, tearoff=False)
        self.imagTreViw.bind ("<Button-3>", self.ContainerMenuPop)

    #####  IMAGES menu Function
    def GetImageID(self):
        selectedimage = str (self.imagTreViw.item (self.imagTreViw.focus ()))
        return selectedimage [78:90]

    def GetImageList(self):
        for i in self.imagTreViw.get_children ():  # clear the old list form screen
            self.imagTreViw.delete (i)
        os.system('docker images > imagelist.dat')
        try:
            df = pd.read_csv("imagelist.dat")

        except ValueError:
            tk.messagebox.showerror("Information", "The File you have entered is invalid")
            return None

        df_rows = df.to_numpy ().tolist ()  # turns the dataframe into a list of lists
        for row in df_rows:
            self.imagTreViw.insert ("", "end", values=row)  # inserts each list into the treeview

        self.imagInfoLbl.configure (text="Please Choose a Container and right Click to select Action")

    def RunImage(self):
        imageID = self.GetImageID ()
        os.system('gnome-terminal -- bash -c "docker run -it  {0} /bin/bash"'.format(imageID))

    def DownloadImage(self):

        answer = simpledialog.askstring ("Download Image", "Please Enter the image name ")
        if answer is not None:
            try:
                os.system ("docker pull {0}".format (answer))
            except:
                pass


        else:
            print ("You don't have a first name?")

    def CreateImage(self):
        pass

    def UploadImage(self):
        pass
    def DeleteImage(self):
        imageID = self.GetImageID()
        if messagebox.askokcancel("Delete Image", "Are you sure you want to Delete Image?"):
            try:
                os.system('docker image rm {0}'.format(imageID))
                self.imagTreViw.delete(self.imagTreViw.selection())
                self.GetImageList()
            except:
                messagebox.showerror ("error", "Cannot Delete Image")

    ###Image Right click menu ###


    def CreatImagePopMenu(self):
        self.DeleteImageMenu()
        if self.GetImageID() != "":
            self.imagPopMenu.add_command (label="create image(New Docker)", command=self.CreateImage)
            self.imagPopMenu.add_command (label="download image", command=self.DownloadImage)
            self.imagPopMenu.add_command (label="run image", command=self.RunImage)
            self.imagPopMenu.add_command(label="Upload Image", command=self.UploadImage)
            self.imagPopMenu.add_command (label="delete image", command=self.DeleteImage)

    def DeleteImageMenu(self):
        self.imagPopMenu.delete (0, 20)

    def ContainerMenuPop(self, e):
        try:
            self.imagPopMenu.place_forget ()
            self.CreatImagePopMenu ()
        except Exception:
            self.CreatImagePopMenu()
        self.imagPopMenu.tk_popup (e.x_root, e.y_root)
