#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys

def doesPrefixExist(pref,args):
    '''
    Return's True if the prefix
    exists
    '''
    for i in args:
        if(i.strip()==pref):
            return True
    return False


def getDataFromPrefix(pref,args):
    '''
    Searches for the prefix and returns
    the data from it
    '''
    for i in range(0,len(args)):
        if(args[i].strip()==pref):
            return args[i+1]
    return None
