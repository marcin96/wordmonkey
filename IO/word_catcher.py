#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import os
import sys
import string
import re

def isRightWordConstruct(line):
    '''
    Checks if the line has correct chars
    '''
    match = re.match("^[ABCDEFGHJKLMOPQRSTUVWXYZ-]*$", line)
    return match is None

def hastherightSize(line):
    '''
    Checks if the line has
    the size of a word
    '''
    if(len(line)<2 and len(line)<20):
        return False
    else:
        return True

def isGerman(line):
    '''
    looks if the word has signs that are
    allowed in the german language.
    '''
    in_german = "äöüß-".join(string.ascii_lowercase)
    for i in line:
        if(i not in in_german):return False
    return True

def onlyVokal(line):
    '''
    Looks if the line has only vokals
    '''
    match = re.match("^[AEOIUÄÖÜY-]*$",line)
    return match is not None

def onlyKonsonant(line):
    '''
    Looks if the line has only konsonants
    '''
    match = re.match("^[BCDGKLMNPQRSTVWXZJH-]*$",line)
    return match is not None

def isGermanWord(line,acceptedSPchars=""):
    '''
    checks if the line is a word
    '''
    if(isinstance(line,str)==False):
        return [False,"Wrong Type Error should be string"]
    line = line.strip()
    if(line == "" or line == " "):
        return [False,"line is empty"]
    if(isRightWordConstruct(line)!=True):
        return [False,"Word has forbidden chars"]
    if(hastherightSize(line)!=True):
        return [False,"Word is to big or to small"]
    if(isGerman(line)!=True):
        return [False,"It contians forbidden chars in german"]
    if(onlyVokal(line)==True):
        return [False,"Only Vokals"]
        None
    if(onlyKonsonant(line)==True):
        return [False,"Only Konsonants"]
        None
    return [True,""]
    
if __name__ == "__main__":
    print(isGermanWord(sys.argv[1]))
