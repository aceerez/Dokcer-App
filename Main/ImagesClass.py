import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog
import os
import ContainerClass
import time
import webbrowser


class Images:
    def __init__(self, master, cont: ContainerClass):

        # This is the frame for the Images Treeview
        self.imagTreeFrame = tk.LabelFrame(master, text="Images list", labelanchor="n")
        self.imagTreeFrame.place(height=250, width=600, rely=0.6, relx=0.0)

        self.cont = cont

        # This is the frame for the info for Images and its action
        '''
        self.imagInfoFrame = tk.LabelFrame (master, text="Images INFO")
        self.imagInfoFrame.place (height=75, width=400, rely=.48, relx=0)

        self.imagInfoLbl = ttk.Label (self.imagInfoFrame, text="Press to Load Images List")
        self.imagInfoLbl.place (rely=0, relx=0)
        self.imagLodlistBtn = tk.Button (self.imagInfoFrame, text="Load Images List",
                                         command=lambda: self.GetImageList ())
        self.imagLodlistBtn.place (rely=0.5, relx=0)
        '''
        ##Option Box
        self.optionFrame = tk.LabelFrame(master, text="Image Option", labelanchor='n')
        self.optionFrame.place(height=250, width=160, rely=0.60, relx=0.61)
        newImageBtn = tk.Button(self.optionFrame, text="Create New Image", command=self.CreateImage)
        newImageBtn.place(rely=0.1, relx=0.0)
        loadImageBtn = tk.Button(self.optionFrame, text="Download  Image  ", command=self.DownloadImage)
        loadImageBtn.place(rely=0.4, relx=0.0)
        uploadImageBtn = tk.Button(self.optionFrame, text="   Upload  Image    ", command=self.UploadImage)
        uploadImageBtn.place(rely=0.7, relx=0.0)
        '''
        self.hubUserNamelbl = tk.Label(self.upDnFrame, text="User Name")
        self.hubUserNamelbl.place(rely=0.2, relx=0.)
        self.hubPasswordlbl = tk.Label(self.upDnFrame, text="PassWord")
        self.hubPasswordlbl.place(rely=0.5, relx=0.1)
        self.hubUserNameEntry = tk.Entry()
        self.hubUserNameEntry.place(rely=0.425, relx=0.76)
        self.hubUserPassWordEntry = tk.Entry()
        self.hubUserPassWordEntry.place(rely=0.475, relx=0.76)
        '''

        # craete Image tree View

        self.imagTreViw = ttk.Treeview(self.imagTreeFrame, selectmode="browse")  # This is the Treeview Widget
        column_list_account = ["REPOSITORY", "TAG", "Image ID", "CREATED", "SIZE"]  # These are our headings
        self.imagTreViw['columns'] = column_list_account  # We assign the column list to the widgets columns
        self.imagTreViw["show"] = "headings"  # this hides the default column..

        for column in column_list_account:  # foreach column
            self.imagTreViw.heading(column, text=column)  # let the column heading = column name
            self.imagTreViw.column(column, width=50)  # set the columns size to 50px

        self.imagTreViw.place(relheight=1,
                              relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).
        self.imagtreescroll = tk.Scrollbar(self.imagTreeFrame)  # create a scrollbar
        self.imagtreescroll.configure(command=self.imagTreViw.yview)  # make it vertical
        self.imagTreViw.configure(yscrollcommand=self.imagtreescroll.set)  # assign the scrollbar to the Treeview Widget
        self.imagtreescroll.pack(side="right", fill="y")  # make the scrollbar fill the yaxis of the Treeview widget

        self.imagPopMenu = Menu(master, tearoff=False)
        self.imagTreViw.bind("<Button-3>", self.ContainerMenuPop)

    #####  IMAGES menu Function
    def GetImageName(self):
        selectedimage = str(self.imagTreViw.item(self.imagTreViw.focus()))
        find_start = selectedimage.find("['")

        if find_start != -1:
            imagName = selectedimage[find_start + 2:selectedimage.find("',", find_start) - 2]
            return imagName
        else:
            return ""

    def GetListDate(self):

        def InfoInsert(cmd):
            row = 0
            os.system(cmd)
            file = open("imagelist.dat")
            for i in file:
                imagelist[row].append(i)
                row += 1

        self.row = 0

        imagelist = []
        os.system("docker images --format '{{.Repository}}' > imagelist.dat ")
        file = open("imagelist.dat")
        for i in file:
            imagelist.insert(self.row, [i])
            self.row += 1

        cmd = "docker images --format '{{.Tag}}' > imagelist.dat"
        InfoInsert(cmd)
        cmd = "docker images --format '{{.ID}}' > imagelist.dat"
        InfoInsert(cmd)
        cmd = "docker images --format '{{.CreatedAt}}' > imagelist.dat"
        InfoInsert(cmd)
        cmd = "docker images --format '{{.Size}}' > imagelist.dat"
        InfoInsert(cmd)
        return imagelist

    def GetImageList(self):
        for i in self.imagTreViw.get_children():  # clear the old list form screen
            self.imagTreViw.delete(i)
        os.system('docker images -a > imagelist.dat')
        try:
            imagelist = self.GetListDate()
        except ValueError:
            tk.messagebox.showerror("Information", "The File you have entered is invalid")
            return None

        for row in imagelist:
            self.imagTreViw.insert("", "end", values=row)  # inserts each list into the treeview

    def RunImage(self):
        imageName = self.GetImageName()
        selectedimage = (self.imagTreViw.item(self.imagTreViw.focus()))
        imageTag = selectedimage.get('values')[1]

        if messagebox.askyesno("Use Ports?","Do you want to Run this Image with PORTS?\n (Select 'No' to Run with Bash)"):
            ports = simpledialog.askstring("","Enter Image Port , use format XX:XX")
            os.system('gnome-terminal -- bash -c "docker run -d -p {0} {1}:{2} "'.format(ports, imageName, imageTag))
        else:
            os.system('gnome-terminal -- bash -c "docker run -it {0}:{1} "'.format(imageName, imageTag))
            time.sleep(2)
        ContainerClass.Container.GetContainerList(self.cont)

    def DownloadImage(self):
        def OpenUrl():
            webbrowser.open_new("https://hub.docker.com/search?type=image")

        def DownloadCmd(e):
            cheackLen = len(self.imagTreViw.get_children())
            os.system("docker pull {0}".format(self.imageNameEntry.get()))
            if self.CheakListChange(cheackLen):
                messagebox.showinfo("Successes", "Image Downloaded Successfully ")
                downloadTop.destroy()
            else:
                messagebox.showerror("ERROR", "ERROR! Can not download image.\nCheck image name again ")
                downloadTop.destroy()

        self.GetImageList()
        downloadTop = Toplevel()
        downloadTop.geometry("{0}x{1}+{2}+{3}".format(400, 400, 700, 400))
        infolbl = tk.Label(downloadTop, text="Please Enter the image name.", font=('Arial', 15))
        infolbl.place(rely=0, relx=0.15)
        self.imageNameEntry = tk.Entry(downloadTop, font=("Arial", 15))
        self.imageNameEntry.place(rely=0.1, relx=0.2)

        searchLbl = Label(downloadTop, text="You can search Images in:\n Docker Hub ", font=("", 13))
        searchLbl.place(rely=0.2, relx=0.2)
        searcBtn = Button(downloadTop, text="HERE", command=OpenUrl)
        searcBtn.place(rely=0.32, relx=0.4)
        self.imageNameEntry.bind("<Return>", DownloadCmd)

    def CreateImage(self):
        path = filedialog.askopenfilename(initialdir="/home/",
                                              title="Select Only A Docker File")

        filename = os.path.split(path)[1]
        imageName = simpledialog.askstring("Image Name", "Enter Image Name")
        self.GetImageList()
        cheackLen = len(self.imagTreViw.get_children())
        while True:
            if imageName != "":
                tagName = simpledialog.askstring("Tag Name", "Enter Tag Name or leave empty")
                if tagName == "":
                    os.system('docker build -t="{0}" . -f {1}'.format(imageName,path))
                else:
                    os.system('docker build -t="{0}:{1}" . '.format(imageName, tagName))

                if self.CheakListChange(cheackLen):
                    ContainerClass.Container.GetContainerList(self.cont)
                    messagebox.showinfo("Successes", "Image Created Successfully")

                    break
                else:
                    messagebox.showerror("ERROR", "ERROR! Can not Creat image.\nCheck DockerFile or Name ")
                    break

            else:
                imageName = simpledialog.askstring("Image Name", "Enter Image Name")

    def CheakListChange(self, cheackLen):
        self.GetImageList()
        if cheackLen != len(self.imagTreViw.get_children()):
            return True
        else:
            return False

    def UploadImage(self):
        pass

    def DeleteImage(self):
        cheackLen = len(self.imagTreViw.get_children())
        selectedimage = (self.imagTreViw.item(self.imagTreViw.focus()))
        imageID = selectedimage.get('values')[2]

        if messagebox.askokcancel("Delete Image", "Are you sure you want to Delete Image?"):
            try:
                os.system('docker image rm -f {0}'.format(imageID))
                if self.CheakListChange(cheackLen):
                    messagebox.showinfo("", "Image Deleted!")
                else:
                    messagebox.showerror("", "Cannot Delete Image!\n"
                                             "Image may be in use")

            except:
                messagebox.showerror("error", "Cannot Delete Image")

    def DeleteAllImage(self):
        if messagebox.askokcancel("Delete All Images", "Are you sure you want to Delete all Images?"):
            try:
                os.system('docker rmi -f $(docker images -a -q)')
                self.GetImageList()
            except:
                messagebox.showerror("error", "Cannot Delete Images")

    ###Image Right click menu ###

    def CreatImagePopMenu(self):
        self.DeleteImageMenu()

        if self.GetImageName() != "":
            self.imagPopMenu.add_command(label="create image(New Docker)", command=self.CreateImage)
            self.imagPopMenu.add_command(label="download image", command=self.DownloadImage)
            self.imagPopMenu.add_command(label="run image", command=self.RunImage)
            self.imagPopMenu.add_command(label="Upload Image", command=self.UploadImage)
            self.imagPopMenu.add_command(label="delete image", command=self.DeleteImage)

    def DeleteImageMenu(self):
        self.imagPopMenu.delete(0, 20)

    def ContainerMenuPop(self, e):
        try:
            self.imagPopMenu.place_forget()
            self.CreatImagePopMenu()
        except Exception:
            self.CreatImagePopMenu()
        self.imagPopMenu.tk_popup(e.x_root, e.y_root)
