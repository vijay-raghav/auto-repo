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
    chdir(repo)
except:
    print repo + " does not exist."
    exit()

url = "https://github.com/%s/" % handle

commands = [
    "git init",
    "git add .",
    "git commit -m \"Initial Commit\"",
    "curl -u %s https://api.github.com/user/repos -d \'{\"name\:\%s\"}\'" % (handle, repo),
    "git remote add origin git@github.com:%s/%s.git" % (handle, repo),
    "git push origin master"
    ]

for command in commands:
    system(command)
