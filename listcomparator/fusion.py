#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

from IO import Importer
from IO import Exporter
from IO import prefile_analyzer
from utils import progressbar
import os

def makeUnique(wordlist):
    '''
    makes the wordlist unique.
    '''
    if(wordlist!=None and len(wordlist)>1):
        if(isinstance(wordlist[0],list)):
            #With 2 dimensions
            ret = []
            for index in range(0,len(wordlist)):
                if(wordlist[index] not in wordlist[index+1:len(wordlist)]):
                    ret.append(wordlist[index])
            return ret
                    
        else:
            #With 1 dimension
            return list(set(wordlist))
    else:
        return ["Nothing"]

def fusion(wordlist_one,wordlist_two):
    '''
    fusions two Wordlists together
    '''
    for i in wordlist_two:
        wordlist_one.append(i)
    return makeUnique(wordlist_one)

def fusionListsTogether(directory):
    '''
    Takes all correct files from a directory and returns a unique wordlist.
    '''
    files = Importer.filterOutCorrectFiles(directory)
    rootWordList = makeUnique(Importer.import_words(directory+"\\"+files[0]))
    for i in range(1,len(files)):
        rootWordList = fusion(rootWordList,Importer.import_words(directory+"\\"+files[i]))
        progressbar.printProgress(i,len(files))
    progressbar.printProgress(len(files),len(files))
    return sorted(rootWordList)
