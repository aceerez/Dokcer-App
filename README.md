# Dokcer-App
this App is a Docker command features with a single click .

I call this app doKCer App on purpose  :)

# Introduction
Welcome to Dokcer App .

This app let you control your docker with an easy mouse click.
All you need to do just follows this instruction and start working.

This app was created and tested on ubunto 18.04.
If you have any comments or suggestions, please contact me.

I created this App for my final Project and will upgrade it as I continue to work with it and add more features.

# Requirements
* Linux Machine 

* Available Disk Space Minimum: 2 GB Recommended: 20 .

* Available RAM Minimum: 8 GB  Recommended: 16 . 

* CPU Count	Minimum: 2  Recommended 4+.

NOTE: This App can not run with PuTTY. If you want to run it with putty You need to run an X server on your windows machine and then enable X11 forwarding in your putty session before you log in (see the Connection / SSH / X11 property page in PuTTY). In the past I've used Xming which is free and eXceed which was not. Once you have an X server on the machine you actually are looking at and forward the X connection over the ssh link, it will setup the DISPLAY environment variable on the remote machine so that X clients can communicate back to the display server. Otherwise, without a DISPLAY setup Tk will raise an error - as you will see if you try to run it on PuTTY.
# instructions

INSTALL App & components

Download the files from github at: https://github.com/aceerez/Dokcer-App.git 


Run the App installer in Terminal using the bash command - " bash dockerAppInstall.sh "press 'y' when ask to.
when finished, log out and than log in .

This script install docker and necessary components to run this app

If you get these Errors during installation :

                          E: Could not get lock /var/lib/dpkg/lock – open (11: Resource temporarily unavailable)

                          E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?

That means that your APT service is occupied. 
restart your machine or wait it out.

NOTE: you can use this command to see APT in use.


ps aux | grep -i apt
                                      


* * * *

make sure that everything is install correctly.


#                                                                   Using the Dokcer App 
# Running the app:
# Terminal:
In the Main directory run the app using "python3 dockerApp.py"

# Files manager:
First make sure that you can run files (you can use this tutorial https://askubuntu.com/questions/761365/how-to-run-a-python-program-directly)
and just run the dockerApp.py

# Using the app

The main window is splitted into two, container and images.
in the middle there is a big botton that load all the docker data to the main windows, now you can start working. 

# The bar menu:
The bar menu is located in the top left of the main window and it has two menus.

# File 
* load data:

  Load docker data to the app

* new docker file:

  creat a new dockerfile using nano. 

  fisrt name your file and when finished, save the file using Ctrl+O and then exit using Ctrl+Z.
  the new docker file will be placed in the dockerfiles directory.

* edit docker file:

  edit a docker file using nano, when finished, save the file using Ctrl+O and then exit using Ctrl+Z.

* Exit:

  Exit the App 

# Edit 
* Delete all containers:

     This action will DELETE ALL CONTAINERS . use it carefully.
     
* Delete all Images:

     This action will DELETE ALL Images . use it carefully.

# The Containers window 
After the data is loaded into the container window, select any container form the list and press the right mouse key to open the option menu.
The option in the menu will change according to the container status. 

you can :
* start container.
* stop container.
* pause and unpause container.
* delete container.
* get in the container.

# The Image window
After the data is loaded into the Image window, select any image form the list and press the right mouse key to open the option menu.

* Run image:

Creat a new container with the selected image. you can add ports to the container for cases like NGINX or Apache.
* Upload image :

Let you upload the selected image to your docker hub repo. First enter your user name and then enter your password.

wait for the upload to finish.

* Delete image :

Delete the selected image


# Image option

# Create new image 
* Choose a Docker file 
* Enter your image name 
* Optional: you can add a tag or leave empty for tag "latest"
* Wait for the process to end and then you can run it 

# Download image 
In the popup window enter the name of the image you want to download.
you can press the "Search Docker Hub" botton to go directly to docker hub search page and from there
just copy the image name to the popup window using Ctrl+V and press 'Enter'

# Upload image 
Let you upload the selected image to your docker hub repo.

first enter your user name and then enter your password.

***********************************
Hope you find this app helpful and i will update and upgrade it as I go along 



