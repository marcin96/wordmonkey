#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys
from utils import progressbar

def getLowest(wordA,wordB):
    '''
    '''
    if(len(wordA)<len(wordB)):return len(wordA)
    return len(wordB)

def getGemeinsamkeiten(wordA,wordB):
    '''
    Returns the count of similarities of
    two words.
    '''
    gemeinsam = 0
    nicht_gemeinsam = 0
    c = 0;
    maxim = getLowest(wordA,wordB)
    wordA +=" "
    wordB +=" "
    for i in range(0,maxim):
        if(wordA[i] == wordB[c]):
            gemeinsam+=1
            i=c
        elif(wordA[c] == wordB[i]):
            gemeinsam+=1
            i=c
        elif(wordA[i+1] == wordB[i+1]):
            if(c<maxim):
                c+=1
                continue
            else:return gemeinsam+1
        else:
            if(c<maxim):
                c+=1
            else:return gemeinsam+1
        if(c<maxim):
            c+=1
        else:return gemeinsam+1
    return gemeinsam+1

def extractMpairs(wordList,is2Dim = False,index = 1):
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
            wort1 = wordList[i]
            wort2 = wordList[c]
            if(is2Dim == True):
                wort1 = wordList[i][index]
                wort2 = wordList[c][index]
            if(abs((len(wort1)-len(wort2))) < 2):
                if(getGemeinsamkeiten(wort1,wort2) > getLowest(wort1,wort2)-1):
                    wordmpair.append(wordList[c])
        if(len(wordmpair)>1):
            mpairs.append(wordmpair)
    progressbar.printProgress(len(wordList),len(wordList))
    print("Found ",len(mpairs)," mpairs")
    return mpairs
