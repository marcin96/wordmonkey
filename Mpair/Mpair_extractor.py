#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys
from utils import progressbar
import difflib

def getLowest(wordA,wordB):
    '''
    returns the lowest length of two words.
    '''
    if(len(wordA)<len(wordB)):return wordA
    return wordB

def getHighest(wordA,wordB):
    if(len(wordA)>len(wordB)):return wordA
    return wordB

def getDifferenz(wordA,wordB,differenz):
    '''
    Returns the count of similarities of
    two words.
    '''
    diff = difflib.ndiff(wordA,wordB)
    additions=0
    subtractions = 0
    for i,s in enumerate(diff):
        if(s[0] =="+"):
            additions+=1
        elif(s[0]=="-"):
            subtractions+=1
    if(subtractions>0 and additions>0):
        return abs(additions-subtractions)+differenz
    elif(subtractions>0 and additions==0):return subtractions
    elif(additions>0 and subtractions==0):return additions
    else:return 0
    

def extractMpairs(wordList,is2Dim = False,index = 1,differenz=1):
    '''
    Extracts Mpairs.
    '''
    if(isinstance(wordList,list)!=True): return "Wrong argument"
    if(len(wordList)<2): return "To fiew words"
    mpairs = []
    count = 0
    for i in wordList:
        progressbar.printProgress(count,len(wordList))
        count+=1
        wordmpair=[]
        wordmpair.append(i)
        for c in wordList:
            wort1 = i
            wort2 = c
            if(is2Dim == True):
                wort1 = i[index]
                wort2 = c[index]
            if(abs((len(wort1)-len(wort2))) == differenz):
                if(getDifferenz(wort1,wort2,differenz)== differenz):
                    wordmpair.append(c)
        if(len(wordmpair)>1):
            mpairs.append(wordmpair)
    progressbar.printProgress(len(wordList),len(wordList))
    print("Found ",len(mpairs)," mpairs")
    return mpairs
