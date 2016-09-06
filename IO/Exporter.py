#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys
from utils import progressbar

def export(data,filename,sep=""):
    '''
    Exports the data into file
    '''
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
                        file.write(word)
                        file.write(sep)
                    file.write("\n")
                count += 1
            file.close()
    progressbar.printProgress(len(data),len(data))
    print("exported ",count, " wrods to file ",filename)
    return count

