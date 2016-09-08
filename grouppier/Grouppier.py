#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw
import os
import sys

'''
<Doku>
'''
class Difference():
    From = 0
    To = 0
    shoultBe = ""
    Butis =""


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

def getDifferenceOfWords(word_one,word_two):
    '''
    Returns the difference of two rootWords
    '''
    diff = []
    for charIndex in range(0,len(word_one)):
        if(word_one[charIndex]!=word_two[charIndex]):
            diff.append([charIndex,word_one[charIndex],word_two[charIndex]])
    return diff
    
def isallowedDifference(diff):
    '''
    Checks if the difference between rootwords
    is allowed in german.
    '''
    allowedPos = [2,5] #Min - Max
    allowed = "a:ä,o:ö,u:ü,i:ie,i:e"
    allowed = allowed.split(",")
    for i in allowed:
        i = i.split(":")
    for d in diff:
        
    
def isTheSame(wordlistOne,wordlistTwo):
    '''
    '''
    for i in wordlistOne:
        for w in wordlistTwo:
            if(i==w):
                return True
            #else:
                #diff = getDifferenceOfWords(i,w)
                #if(isallowedDifference(diff)):
                    #return True
    return False

def isRootPart(wort,wort2):
    '''
    Looks if the rootpart of word is
    a part of word2
    '''
    if(isTheSame(removePostfix(wort),removePostfix(wort2))):
        return True
    if(removePrefix(wort) == removePrefix(wort2)):
        return True
    return False
    
def gruppiere(liste):
    '''
    Puts the same word in differend variants into a list.
    '''
    gruppen = []
    tabu = []
    for index in range(0,len(liste)):
        theSameWord = []
        theSameWord.append(liste[index])
        if(liste[index] in tabu):continue
        for tocomI in range(index+1,len(liste)):
            if(liste[tocomI] in tabu):continue
            if(isRootPart(liste[index],liste[tocomI])):
                if(liste[tocomI] not in theSameWord):
                    theSameWord.append(liste[tocomI])
                    tabu.append(liste[tocomI])
        if(len(theSameWord)>1):
            gruppen.append(theSameWord)
    print("Found ",len(gruppen)," groups")
    return gruppen
