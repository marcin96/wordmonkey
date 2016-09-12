#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import os.path
import sys
from utils import progressbar

def isFileEmpty(filename):
    '''
    Is the file empty
    '''
    return os.stat(filename).st_size == 0

def doesFileExist(filename):
    '''
    Does this file exist
    '''
    return os.path.isfile(filename)

def checkFileName(filename):
    '''
    Checks if the file exists and is empty or not.
    '''
    if(doesFileExist(filename)):
        print("File <",filename,"> exists")
        if(isFileEmpty(filename)==False):
            print("File ", filename," is not empty")
            return False
    return True

def changeFilename():
    '''
    User can chose a new filename for the output.
    '''
    return input("New Filename:>")

def export(data,filename,sep=""):
    '''
    Exports the data into file
    '''
    if(len(data)==0):
        print("There is nothing to export")
        return
    if(checkFileName(filename)==False):
        filename = changeFilename()
    count = 0
    if(isinstance(data,list)):
        if(len(data)>0):
            file = open(filename,"a",encoding="UTF-8")
            for i in data:
                progressbar.printProgress(count,len(data))
                if(isinstance(i,str)):
                    file.write(i)
                    file.write(sep)
                    file.write("\n")
                elif(isinstance(i,list)):
                    for word in i:
                        if(isinstance(word,list)):
                            for w in word:
                                file.write(w)
                                file.write(" ")
                        else:
                            file.write(word)
                            file.write(sep)
                    file.write("\n")
                count += 1
            file.close()
    progressbar.printProgress(len(data),len(data))
    print("exported ",count, " wrods to file ",filename)
    return count

