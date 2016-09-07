#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw
import os
import sys
#---------
from IO import prefile_analyzer
from IO import word_catcher

def filterOutCorrectFiles(directory,extens=".txt",encoding="UTF-8"):
    '''
    Filters out files with the .txt extension.
    '''
    files = []
    for name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, name)):
            if(prefile_analyzer.isFileInOrder(name)):
                files.append(name)
    return files

def import_words(filename,startindex = 0,endWord = "#END"):
    '''
    Imports words from file
    First checks if file is in Order
    The it checks line for line if it
    has the right pattern
    '''
    words = []
    report = prefile_analyzer.isFileInOrder(filename)
    port = open("log.txt","a")
    port.write(filename)
    if(report[0]):
        count = 0
        with open(filename,encoding="UTF-8") as file:
            for line in file:
                if(count>startindex):
                    line = line.lower().strip()
                    if(line.lower() == endWord.lower()):break
                    if(";" in line):
                        #Also has phonetic
                        port.write("Found Phonetics")
                        word = line.split(";")[0]
                        phonetic = line.split(";")[1]
                        if("," in word):
                            wordt = word.split(",")
                            w = ""
                            for i in wordt:
                                if(word_catcher.isGermanWord(str(i.strip()))[0]==True):
                                    w+=i
                            words.append([w,phonetic])
                        else:
                            ret = word_catcher.isGermanWord(str(word))
                            if(ret[0]==True):words.append([word,phonetic])
                    else:
                        #normal import
                        if("," in line):
                            worte = line.split(",")
                            wt = ""
                            for i in worte:
                                if(word_catcher.isGermanWord(str(i))[0]):
                                    wt+= i + ","
                            words.append(wt[:-1])
                        else:
                            ret = word_catcher.isGermanWord(str(line))
                        if(ret[0]==True):words.append(line)
                        else:
                            try:
                                port.write(str(line) +">" + str(ret[1])+"\n")
                            except:
                                None
                count+=1
    else:
        for i in report:
            port.write(str(i))
            port.write("\n")
    port.close()
    print("imported ", len(words)," from file [",filename,"]")
    return words
