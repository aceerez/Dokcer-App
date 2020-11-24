#!/bin/bash

# * Docker Installation
# *******************************
echo Update Local Database
sudo apt-get update

chmod +x ./Main/dockerApp.py

echo Download Dependencies
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

echo Add Docker’s GPG Key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

echo Install the Docker Repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"

echo Update Repositories
sudo apt-get update

echo Install Latest Version of Docker
sudo apt-get install docker-ce

echo install python3 and components 
sudo apt install python3 python3-pip -y
sudo apt-get install python3-tk

echo Create the docker group.
sudo groupadd docker

echo Adding user ${USER} to the docker group.
sudo usermod -aG docker ${USER}

echo
echo LOGOUT AND LOG BACK IN
echo
