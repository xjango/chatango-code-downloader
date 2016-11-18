import sys

import requests
import os
import random
import time

#store folder name so it doesn't create another one.
folder = "";
rn = random.randrange(1000,10000);
files = ["full.jpg","msgbg.xml","mod1.xml","mod2.xml"];
directory = "/path/to/diir"; #remember to set this path else it won't work. the path needs to be the same path where the file is.

def download(username):
	f = open("logs.txt", "a");
	tmp_folder = str("%d_%s_tmp" % (rn,username));
	folder = tmp_folder 
	os.popen("sudo mkdir " + folder); #create tmp dir
	for item in files:
		os.popen("sudo wget -q -O "+ directory + folder + "/" + item + " http://st.chatango.com/profileimg/" + username[0:1] + "/" + username[1:2] + "/" + username + "/" + item + ""); 
	os.popen("sudo zip -r " + folder + " " + folder) #zips everything from the tmp folder with the same name.
	os.popen("sudo rm -r " + folder)
	print ("Finished Downloading files for " + username);
	

def check(username):
	url = requests.get("http://fp.chatango.com/profileimg/" + username[0:1] + "/" + username[1:2] + "/" + username + "/mod1.xml");
	l = len(url.text)
	x = url.text[l - 6:] #checking to see if </mod> is present indicating a proper file with real data in it.
	if x == "</mod>":
		download(username);
	else:
		print ("No real data to collect for " + username)
	

check(sys.argv[1]);

