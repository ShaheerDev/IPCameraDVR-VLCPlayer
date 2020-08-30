#Import libaries
import os
import platform  #To identify the OS
import subprocess  #To start VLC
from subprocess import Popen, PIPE, STDOUT
from subprocess import DEVNULL    # To keep the script running after subprocess is called

#DVR inputs
ip_adr = input("What is your DVR's ip address?: ")
port = input("What is your DVR's RTSP port? (it should be 554 or else): ")
username = input("What is your DVR's username? (The default is admin): ")
password = input("What is your DVR's password?: ")
linkurl = "rtsp://" + username +":" + password + "@" + ip_adr + ":" + port +"/Streaming/channels/1/"

#Identify OS
nameos = platform.system()

if nameos == "Linux":  # For Linux
    cmd='vlc' + " " + linkurl;
    print("Your DVR rtsp link is: " + linkurl)
    Popen([cmd], stderr=subprocess.DEVNULL, stdin=PIPE, shell=True)
else:   # For windows
    cmd='vlc' + " " + linkurl;
    print("Your DVR rtsp link is: " + linkurl)
    Popen([cmd], stderr=subprocess.DEVNULL, stdin=PIPE, shell=True)
