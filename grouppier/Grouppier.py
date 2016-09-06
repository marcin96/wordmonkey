#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw
import os
import sys

'''
<Doku>
'''

def getMinim(wort1,wort2):
    '''
    return the lowest word lenght
    '''
    if(len(wort1)>len(wort2)):
        return len(wort2)
    return len(wort1)

def removePostfix(wort):
    '''
    removes the postfixes in the german language
    '''
    Endungen="en,st,te,nd,et,le,elt,n,t,e"
    Endungen = Endungen.split(",")
    endFrei=[]
    for e in Endungen:
        if(wort[-len(e):]==e):
            endFrei.append(wort[:len(wort)-len(e)])
    sorted(endFrei)
    if(len(endFrei)>0):
        return endFrei
    else:
        return wort

def removePrefix(wort):
    '''
    Removes prefix of german words.
    '''
    if(wort[:2]=="ge"):
        return wort[-(len(wort)-2):]
    return wort

def isRootPart(wort,wort2):
    '''
    Looks if the rootpart of word is
    a part of word2
    '''
    diff = abs(len(wort)-len(wort2))
    if(diff>3 or diff == 0):return False
    if(removePostfix(wort) == removePostfix(wort2)):
        return wort2
    if(removePrefix(wort) == removePrefix(wort2)):
        return wort2
    
def gruppiere(liste):
    '''
    Puts the same word in differend variants into a list.
    '''
    gruppen = []
    for index in range(0,len(liste)):
        theSameWord = []
        theSameWord.append(liste[index])
        for tocomI in range(index+1,len(liste)):
            if(isRootPart(liste[index],liste[tocomI])):
                theSameWord.append(liste[tocomI])
        if(len(theSameWord)>1):
            gruppen.append(theSameWord)
    return gruppen
