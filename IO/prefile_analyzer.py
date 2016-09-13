#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys


def isRightEncoding(filename):
    '''
    checks if the file has utf8 encoding
    '''
    try:
        fh = open(filename,"r",encoding = "UTF-8")
        fh.close()
        return True
    except:
        return False

def getFileSize(filename):
    '''
    returns the filesize
    '''
    return os.path.getsize(filename)

def isFileEmpty(filename):
    '''
    '''
    if(getFileSize(filename)==0):
        return True
    return False

def isFileInOrder(filename):
    '''
    '''
    print("Analyzing File ",filename)
    if(os.path.isfile(filename)!=True):
        #Does the file exist
        print("[fail] File does not Exist")
        return [False,"File does not Exist"]
    elif(isFileEmpty(filename)==True):
        print("[fail] The File is empty")
        return [False,"The File is empty"]
    elif(filename.split(".")[1] not in ["txt","TXT"]):
        #has it the right extension
        print("[fail] is not a text file")
        return [False,"is not a text file"]
    elif(isRightEncoding(filename)!=True):
        #is the coding right
        print("[fail] Wrong encoding must be utf-8")
        return [False,"Wrong encoding must be utf-8"]
    elif(os.access(filename,os.R_OK)!=True):
        #do we have the persmission to read
        print("[fail] Don't have permission to read")
        return [False,"Don't have permission to read"]
    print("\r[smile] Everything OK!")
    return [True,""]


if __name__=="__main__":
    isFileInOrder(sys.argv[1])
