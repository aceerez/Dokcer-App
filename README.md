# Dokcer-App
this App is a Docker command features with a single click .

# Introduction
Welcome to Docker App .

This app let you control your docker with an easy mouse click.
All you need to do just follows this instruction and start working.

this app was created and tested on ubunto 18.04.
If you have any comments or suggestions, please contact me.

I created this App for my final Project and will upgrade it as I continue to work with it and add more features.

# Requirements
Available Disk Space Minimum: 2 GB Recommended: 20 .
Available RAM Minimum: 8 GB  Recommended: 16 . 
CPU Count	Minimum: 2  Recommended 4+.

# instructions

INSTALL App & components

Download the files from github at: https://github.com/aceerez/Dokcer-App.git 


Run the App installer in Terminal using the bash command - " bash dockerAppInstall.sh "press 'y' when ask to.
when finished, log out and than log in .

this script install docker and necessary components to run this app

If you get these Errors during installation :

                          E: Could not get lock /var/lib/dpkg/lock – open (11: Resource temporarily unavailable)

                          E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?

That means that your APT service is occupied. 
restart your machine or wait it out.
NOTE: you can use this command to see APT in use.


ps aux | grep -i apt
                                      



make sure that evrything is insatll corectly.


# Using the Dokcer App 
# Running the app:
Terminal - in the Main follder run the app using "python3 dockerApp.py"

Files manager - first make sure that you can run files (you can use this tutrial https://askubuntu.com/questions/761365/how-to-run-a-python-program-directly)
and just run the dockerApp.py

# Using the app

The main window is splited into two , container and images.
in the midelle there is a big botton that load all the docker data to the main windows, now you can start working . 

The bar menu:

The bar menu is located in the top left of the main window and it has two menu .
# File 
# load data - load docker data to the app
# new docker file:
creat a new dockerfile using nano. 
fisrt name your file and when finished, save the file using Ctrl+O and then exit using Ctrl+Z.
the new docker file will be placed in the dockerfiles directory.

# edit docker file:
edit a docker file using nano,when finished, save the file using Ctrl+O and then exit using Ctrl+Z.

# Edit 
# Delete all containers - this action will DELELTE ALL CONTAINERS . use it carefully.
# Delete all Images - this action will DELELTE ALL Images . use it carefully.

# The Containers window 
After the data is loaded into the container window, select any container form the list and press the right mouse key to open the option menu.
the option in the menu will change according to the container status. 
you can : start,stop,pause and unpause,delelet and get in the container.

# The Image window




# Trubleshoting 

   Error                                                   sulotion

B} Can't execut app from files manager                          3)https://askubuntu.com/questions/761365/how-to-run-a-python-program-directly

