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
    print("Making Wordlist unique")
    if(wordlist!=None and len(wordlist)>1):
        if(isinstance(wordlist[0],list)):
            #With 2 dimensions
            ret = []
            for index in range(0,len(wordlist)):
                progressbar.printProgress(index,len(wordlist))
                if(wordlist[index] not in ret):
                    ret.append(wordlist[index])
            return ret
                    
        else:
            #With 1 dimension
            ret = []
            for i in wordlist:
                if(i not in ret):
                    ret.append(i)
            return ret
            
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
