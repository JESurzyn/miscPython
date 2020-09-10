#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:05:29 2020

@author: jordan
"""

#DESCRIPTION:
    #NAME: courseraMove.py
    #PURPOSE: To move and rename files downloaded from Coursera Jupyter
    #Notebook learning platform.
    
import shutil, os, re, sys
import pyinputplus as pyip
from pathlib import *

#this will be run from terminal

#the origin string
originPathString = Path().home()/'Downloads'
#grab all files in Downloads with utf-8 in name
filesList = [i.as_posix() for i in list(originPathString.glob('*utf-8*'))]

if len(filesList) == 0:
    print('\nno files found, quitting...')
    sys.exit()   

for i in filesList:
    print(i)
 
moveAndName = pyip.inputYesNo('\nMove and edit names for these files?', timeout=100)

if moveAndName == 'yes':
    #ask user for destination path
    while True:
        classFolderString = input('\ninput class folder\n')
        if '/' in classFolderString:
            print("don't include any slashes, just the name by itself. try again")
            continue
        classString = Path.home()/classFolderString
        if classString.exists():
            break
        else:
            print("that folder doesn't exist, try again or create the folder")
    
    while True:
        weekFolderString = input('\ninput the week folder name\n')
        if '/' in weekFolderString:
            print("don't include any slashes, just the name by itself. try again")
            continue
        fullDestinString = Path.home()/classFolderString/weekFolderString
        if fullDestinString.exists():
            break
        else:
            print("that folder doesn't exist, try again or create the folder")
    
    destinPath = Path.home()/classFolderString/weekFolderString
    
    destinPathString = destinPath.as_posix()
    
    #move the files into the new folder and change name          
    utfRegex = re.compile(r'(utf-8\'\')(.*)')
    
    for i in filesList:
        base = os.path.basename(i)
        mo = utfRegex.search(base)
        changedName = mo.group(2)
        destinPlusName = destinPathString +'/'+changedName
        shutil.move(i, destinPlusName)
    
    print('\nfollowing files moved:')
    for i in os.listdir(destinPathString):
        print(i)

else:
    print('\naborted')