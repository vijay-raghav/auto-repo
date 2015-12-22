#! /usr/bin/env python
'''
Usage 
    python auto-repo.py username repo
'''
import sys
from os import chdir, system

args = sys.argv

if len(args) <= 2:
    print "Usage: python auto-repo.py username repo"
    exit()

handle = args[1]
repo = args[2]

try:
    os.chdir(repo)
except:
    print repo + " does not exist."
    exit()

url = "https://github.com/" + handle + "/"

cmds = [
    "git init",
    "git add .",
    "git commit -m \"Initial Commit\"",
    "curl -u " + handle +  " https://api.github.com/user/repos -d " + "\'{\"name\":" + "\"" + repo + "\"}\'",
    "git remote add origin git@github.com:" + handle + "/" + repo + ".git",
    "git push origin master"
    ]

for cmd in cmds:
    os.system(cmd)
