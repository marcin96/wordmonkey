#
#
#
import os
import sys
from IO import Importer

def getDifference(file_one,file_two):
    '''
    Analyzes two wordLists and returns the difference
    of them.
    '''
    list_one = Importer.import_words(file_one)
    list_two = Importer.import_words(file_two)
    diff_lenght = abs(len(list_one)-len(list_two))
    not_similar=0
    for i in list_one:
        if(i not in list_two):
            not_similar+=1
    return not_similar


if __name__=="__main__":
    '''
    Not supported
    '''
    None
