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
    return list(set(wordlist)) 

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
