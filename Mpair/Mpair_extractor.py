#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys
from utils import progressbar


def getGemeinsamkeiten(wordA,wordB):
    '''
    Returns the count of similarities of
    two words.
    '''
    gemeinsam = 0
    nicht_gemeinsam = 0
    wordB+=" "
    for i in range(0,len(wordA)):
        if(wordA[i] == wordB[i]):
            gemeinsam+=1
        else:
            nicht_gemeinsam +=1
            if(nicht_gemeinsam>1):return 0
    return gemeinsam

def extractMpairs(wordList):
    '''
    Extracts Mpairs.
    '''
    if(isinstance(wordList,list)!=True): return "Wrong argument"
    if(len(wordList)<2): return "To fiew words"
    mpairs = []
    for i in range(0,len(wordList)):
        progressbar.printProgress(i,len(wordList))
        wordmpair=[]
        wordmpair.append(wordList[i])
        for c in range(i+1,len(wordList)):
            if(abs((len(wordList[i])-len(wordList[c]))) < 2):
                if(abs((getGemeinsamkeiten(wordList[i],wordList[c])-len(wordList[c]))) < 2):
                    wordmpair.append(wordList[c])
        if(len(wordmpair)>1):
            mpairs.append(wordmpair)
    progressbar.printProgress(len(wordList),len(wordList))
    print("Found ",len(mpairs)," mpairs")
    return mpairs


if __name__ =="__main__":
    '''
    Not really suported
    '''
    None
