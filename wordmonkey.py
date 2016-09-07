#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys
from utils import prefixManager
from IO import Importer
from IO import Exporter
from listcomparator import fusion
from listcomparator import comparator
from Mpair import Mpair_extractor
from grouppier import Grouppier
from crawler import WordSpyder
from utils import ressource_manager
import time
import datetime

def printOutput(out):
    '''
    prints the output
    '''
    for i in out:print(i)

def gettimeMSG():
    '''
    Returns the current date and time
    will be in utils
    '''
    now = datetime.datetime.now()
    return str("["+str(now.year)+","+str(now.month)+","+str(now.day)
    +"] ["+str(now.hour)+":"+str(now.minute)+"]")

def showTermsForAccept(list_lenght,time_faktor,space_faktor):
    '''
    Shows the terms of the called funktion.
    [*]How much time this will need
    [*]How much space this will need
    '''
    print("Runtime: ",ressource_manager.calcTimeNeed(list_lenght,time_faktor))
    print("Space Needed: ",ressource_manager.calcSpaceNeed(list_lenght,space_faktor))
    written = input("Do you accept[y/n]:")
    if(written.lower().strip() in ["yes","y"]):return True
    return False

def doWortExtraction(args):
    '''
    Imports only german words from a file
    with utf-8 encoding and txt extension.
    '''
    print("Word Extraction->")
    print(gettimeMSG())
    ressource_manager.startTime()
    inputfile = prefixManager.getDataFromPrefix("-i",args)
    outputfile = prefixManager.getDataFromPrefix("-o",args)
    startindex = prefixManager.getDataFromPrefix("-stri",args)
    endword = prefixManager.getDataFromPrefix("-end",args)
    #-
    printout = prefixManager.doesPrefixExist("--prntOut",args)
    #-
    if(startindex == None):startindex = 0
    if(endword==None):endword = "#END"
    words = sorted(fusion.makeUnique(Importer.import_words(inputfile,startindex = int(startindex),endWord = endword)))
    if(outputfile == None):outputfile = "out.txt"
    if(printout):printOutput(words)
    if(isinstance(words[0],list)):
        Exporter.export(words,outputfile,sep =";")
    else:
        Exporter.export(words,outputfile)
    print("Took ",ressource_manager.stopTime()," s")
    

def doListCompare(args):
    '''
    Compares wordlist together.
    Can show the difference or
    fussion them together to one file.
    '''
    print("List Compare->")
    print(gettimeMSG())
    ressource_manager.startTime()
    inputdirectory = prefixManager.getDataFromPrefix("-i",args)
    tocomparedir = prefixManager.getDataFromPrefix("-c",args)
    outputfile = prefixManager.getDataFromPrefix("-o",args)
    fus = prefixManager.doesPrefixExist("-f",args)
    diff = prefixManager.doesPrefixExist("-diff",args)
    #-
    printout = prefixManager.doesPrefixExist("--prntOut",args)
    #-
    if(fus==True):
        wordlist = fusion.fusionListsTogether(inputdirectory)
        print("Found "+str(len(wordlist))+" unique words")
        Exporter.export(wordlist,outputfile)
    elif(diff == True):
        difference = comparator.getDifference(inputdirectory,tocomparedir)
        print("Difference:",difference)
    print("Took ",ressource_manager.stopTime()," s")

def doMinimalPairs(args):
    '''
    Extracts mpairs from wordlist
    '''
    print("Minimal Pairs->")
    print(gettimeMSG())
    ressource_manager.startTime()
    inputfile = prefixManager.getDataFromPrefix("-i",args)
    outputfile = prefixManager.getDataFromPrefix("-o",args)
    #-
    printout = prefixManager.doesPrefixExist("--prntOut",args)
    #-
    if(inputfile==0):print("wrong inputfile");return
    words = Importer.import_words(inputfile)
    mpairs = []
    if(isinstance(words[0],list)):
       mpairs = Mpair_extractor.extractMpairs(words,is2Dim = True,index = 1)
    else:
        mpairs = Mpair_extractor.extractMpairs(words)
    if(printout):printOutput(mpairs)
    Exporter.export(mpairs,outputfile,sep=":")
    print("Took ",ressource_manager.stopTime()," s")

def doCrawl(args):
    '''
    Crawls for german words.
    It's possible to crawl a website
    a book.
    or just run the standart function
    of crawling wikipedia.
    '''
    print("Crawl->")
    print(gettimeMSG())
    ressource_manager.startTime()
    inputfile = prefixManager.getDataFromPrefix("-i",args)
    web = prefixManager.getDataFromPrefix("-w",args)
    book = prefixManager.getDataFromPrefix("-b",args)
    #---
    phonetic = prefixManager.doesPrefixExist("-phon",args)
    spell = prefixManager.doesPrefixExist("-spell",args)
    definition = prefixManager.doesPrefixExist("-deff",args)
    #---
    wikipedia = prefixManager.doesPrefixExist("-wikipedia",args)
    count = prefixManager.getDataFromPrefix("-count",args)
    outputfile = prefixManager.getDataFromPrefix("-o",args)
    #-
    printout = prefixManager.doesPrefixExist("--prntOut",args)
    #-
    if(inputfile!=None):
        if(phonetic==True):
            print("[phonetic mode]")
            WordSpyder.getPhonetic(inputfile,outputfile)
        elif(spell==True):
            print("[synthesizer mode]")
            WordSpyder.getSpell(inputfile)
        elif(definition==True):
            print("[definition mode]")
            #--Not Supported at the moment
            None
    elif(web!=None):
        #Crawl from a given website
        #--Not Supported at the moment
        None
    elif(book!=None):
        #Crawl from a book
        print("[book crawl mode]")
        WordSpyder.extractBooks(book)
    elif(wikipedia!=None):
        print("[wikipedia crawl mode]")
        WordSpyder.missionControl("Null")
        print("Files -> /dist")
        #Crawl from wikipedia //standart mode
    print("Took ",ressource_manager.stopTime()," s")

def doGroupier(args):
    '''
    Groups the words:
    Searches for a pattern of one wort
    of on sort and groups them together like
    minimalpairs does.
    '''
    print("grouppier->")
    print(gettimeMSG())
    ressource_manager.startTime()
    inputfile = prefixManager.getDataFromPrefix("-i",args)
    outputfile = prefixManager.getDataFromPrefix("-o",args)
    #-
    printout = prefixManager.doesPrefixExist("--prntOut",args)
    #-
    groups = Grouppier.gruppiere(Importer.import_words(inputfile))
    if(printout):printOutput(groups)
    Exporter.export(groups,outputfile,sep=":")
    print("Took ",ressource_manager.stopTime()," s")
    

def printVersion():
    '''
    shows the version
    '''
    print("Version 1.0")

def showHelp():
    '''
    shows the help message
    '''
    f = open("Readme.md","r")
    hep = f.read()
    print(hep)
    print("For help please read the ReadMe.md file")

def checkCanBeRun():
    '''
    Checks for the right Python version
    '''
    if(sys.version_info<(3,0)):
        print("Please install python >3.0")
        raise "Wrong python version"
        return False
    else:
        return True

def main(args,console=False):
    '''
    Main method of wordMonkey
    '''
    if(console == False):print("[Wordmonkey]")
    if(checkCanBeRun()==False):exit()
    if(len(args)>1):
        if(args[1]=="-wx"):
            #Word filter
            doWortExtraction(args)
        elif(args[1]=="-lc"):
            #Word comparator
            doListCompare(args)
        elif(args[1]=="-mp"):
            #minimalpairs
            doMinimalPairs(args)
        elif(args[1]=="-gp"):
            #Groupier
            doGroupier(args)
        elif(args[1]=="-sort"):
            #Sort
            doWortExtraction(args)
        elif(args[1]=="-crwl"):
            #Crawl
            doCrawl(args)
        elif(args[1] in ["-v","-version"]):
            #Version
            printVersion()
        elif(args[1] in ["-h","-help"]):
            #Help
            showHelp()
        elif(args[1] in ["-bye","-exit","-finish","-end"]):
            print("Ou Revior")
            exit()
        else:
            print("Wrong arguments")
    else:
        if(console==False):
            print("To fiew arguments")
            print("start interpreted mode")
            print(gettimeMSG())
        while(True):
            main(("wordmonkey "+input(">")).split(" "),True)
    print("Log ~[log.txt]")


if __name__== "__main__":
    #Entry Point of Wordmonkey
    try:
        main(sys.argv)
    except KeyboardInterrupt:
            input("<Interrupted>")
