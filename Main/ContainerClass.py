import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog
import pandas as pd
import os


class Container:

    def __init__(self, master):
        # This is the frame for the Container Treeview
        self.contTreeFrame = tk.LabelFrame (master, text="Container list")
        self.contTreeFrame.place (height=250, width=800)

        # This is the frame for the info for container and its action
        self.contInfoFrame = tk.LabelFrame (master, text="Container INFO")
        self.contInfoFrame.place (height=75, width=400, rely=.32, relx=0)

        self.contInfoLbl = ttk.Label (self.contInfoFrame, text="Please Load Container List")
        self.contInfoLbl.place (rely=0, relx=0)
        self.contloadListBtn = tk.Button (self.contInfoFrame, text="Load Container List",
                                          command=lambda: self.GetContainerList ())
        self.contloadListBtn.place (rely=0.5, relx=0)

        # create Container tree View

        self.contTreViw = ttk.Treeview (self.contTreeFrame)  # This is the Treeview Widget
        self.column_list_account = ["CONTAINER ID"]  # These are our headings
        self.contTreViw ['columns'] = self.column_list_account  # We assign the column list to the widgets columns
        self.contTreViw ["show"] = "headings"  # this hides the default column..

        for column in self.column_list_account:  # foreach column
            self.contTreViw.heading (column, text=column)  # let the column heading = column name
            self.contTreViw.column (column, width=50)  # set the columns size to 50px

        self.contTreViw.place (relheight=1,
                               relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).
        self.treescroll = tk.Scrollbar (self.contTreeFrame)  # create a scrollbar
        self.treescroll.configure (command=self.contTreViw.yview)  # make it vertical
        self.contTreViw.configure (yscrollcommand=self.treescroll.set)  # assign the scrollbar to the Treeview Widget
        self.treescroll.pack (side="right", fill="y")  # make the scrollbar fill the yaxis of the Treeview widget

        self.contPopMenu = Menu (master, tearoff=False)
        self.contTreViw.bind ("<Button-3>", self.ContainerMenuPop)

        ####

    ####Container menu Function

    def GetContID(self):
        selectedCont = str(self.contTreViw.item(self.contTreViw.focus()))
        print(str(self.contTreViw.item(self.contTreViw.focus())))
        return selectedCont[38:50]

    def ContainerStatus(self):
        continaerStatus = str(self.contTreViw.item(self.contTreViw.focus()))
        paused = continaerStatus.find("Paused")
        if continaerStatus[123:125] == "Up":
            if continaerStatus[paused:(paused+6)] == "Paused":
                return "Paused"
            else:
                return "Up"
        else:
            return "Exited"

    def GetContainerList(self):
        for i in self.contTreViw.get_children():  # clear the old list form screen
            self.contTreViw.delete(i)
        os.system('docker ps -a > dockerList.dat')
        try:
            df = pd.read_csv("dockerList.dat")

        except ValueError:
            tk.messagebox.showerror("Information", "The File you have entered is invalid")
            return None

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            self.contTreViw.insert("", "end", values=row)  # inserts each list into the treeview
        self.contInfoLbl.configure(text="Please Choose a Container and right Click to select Action")

    def DeleteContainer(self):
        contID = self.GetContID()
        if messagebox.askokcancel("Delete container", "Are you sure you want to Delete container?"):
            try:
                os.system('docker rm -f {0}'.format(contID))
                self.contTreViw.delete(self.contTreViw.selection())
                self.GetContainerList()
            except:
                messagebox.showerror("error", "Cannot Delete Container")

    def StopStartContainer(self):
        contID = self.GetContID()
        if self.ContainerStatus() == "Up":
            os.system('docker stop {0} '.format(contID))
        elif self.ContainerStatus() == "Exited":
            os.system('docker start {0} '.format(contID))
        self.GetContainerList()

    def PauseUnpausecontainer(self):
        contID = self.GetContID()
        if self.ContainerStatus() == "Paused":
            os.system('docker unpause {0} '.format(contID))
        elif self.ContainerStatus() == "Up":
            os.system('docker pause {0} '.format(contID))
        self.GetContainerList()

    def RunContainer(self):
        contID = self.GetContID()
        os.system('docker exec -it  {0} bash'.format(contID))


    ###Container Right click menu ###
    def CreatContainerPopMenu(self):
        self.DeleteMenu()
        self.containerStatus= self.ContainerStatus()
        print(self.containerStatus)
        if self.GetContID() != ", 'open': 0,":

            if self.ContainerStatus() == "Up":
                self.contPopMenu.add_command(label="Stop Container", command=self.StopStartContainer)
                self.contPopMenu.add_command(label="Pause Container", command=self.PauseUnpausecontainer)
                self.contPopMenu.add_command(label="Run Container in terminal ", command=self.RunContainer)
            elif self.ContainerStatus() == "Paused":
                self.contPopMenu.add_command(label="Unpause Container", command=self.PauseUnpausecontainer)
            elif self.ContainerStatus() == "Exited":
                self.contPopMenu.add_command(label="start Container", command=self.StopStartContainer)

            self.contPopMenu.add_command(label="Delete Container", command=self.DeleteContainer)

    def DeleteMenu(self):
        self.contPopMenu.delete(0, 20)


    def ContainerMenuPop(self, e):
        try:
            self.contPopMenu.place_forget()
            self.CreatContainerPopMenu()

        except Exception:
            self.CreatContainerPopMenu()
        self.contPopMenu.tk_popup(e.x_root, e.y_root)

