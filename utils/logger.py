#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw
import os
import sys

'''
<module documentation>
'''

def writeToLog(what,who=None,status="[i]",sep=False):
    '''
    Writes Messages to log.
    '''
    if(what==None):return
    port = open("log.txt","a")
    if(who!=None):
        port.write(who+"\n")
    if(isinstance(what,list)):
        for i in what:
            port.write(status+i+"\n")
    else:port.write(status+what+"\n")
    port.close()
