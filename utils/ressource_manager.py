#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys
import time

startTm = None

def startTime():
    '''
    
    '''
    global startTm
    startTm = int(round(time.time()))

def stopTime():
    '''

    '''
    global startTm
    now = int(round(time.time()))
    return now-startTm

def calcTimeNeed(listlenght,faktor):
    '''
    Calculates the needed time
    '''
    return listlenght * faktor

def calcSpaceNeed(listlenght,faktor):
    '''
    Calculates the needed space
    '''
    return listlength * faktor
