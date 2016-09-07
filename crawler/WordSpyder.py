#Author: chee,stbf
#Python 3.4
#Written for ZHAW
# -*- coding: utf-8 -*-

from IO import Importer
from IO import Exporter
from utils import progressbar
import os
from os import listdir
from os.path import isfile, join
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import time
import random


def getWebsiteSource(url):
    '''
    returns the website html source.
    '''
    try:
        u = urlopen(url)
        return u.read()
    except:
        return None


def removeTrash(data):
    '''
    Removes all tags and blue data.
    '''
    tags = "bpih"
    for i in tags:
        data = data.replace("<"+i+">","")
        data = data.replace("</"+i+">","")
    trash = "=)£!:_;<>{}[]_-+-*/.,\?!\"\'@#$+-*/"
    for i in trash:
        data = data.replace(i,"")
    return data

def remove_duplicates(l):
    '''
    Removes duplicates from list.
    '''
    return list(set(l))

def isWord(word):
    '''
    Checks if the given String is a Word.
    '''
    if(len(word.strip())<2):return False
    forbidden = "1234567890=)(/&%%/*@*#ÀÁÂÆÇÈÉÊËÎÏÔŒÙÛŸ»«<>ĄĆŃÓŚŹŻĘ"
    for i in forbidden:
        if(i.lower() in word.lower()):
            return False
    return True
    

def extractToWordList(source):
    '''
    Extracts the html webpage source
    to a wordlist.
    '''
    source = str(source).split("<p>")
    source = source[1:]
    for i in source:
        i = i.split("<\p>")
    for i in source:
        i = removeTrash(i)
    wordlist =[]
    for i in source:
        t = i.split(" ")
        for w in t:
            if(isWord(w)):
                wordlist.append(removeTrash(w))
    return wordlist

def writeToFile(wordlist,count,name):#Replace with exporter call#
    '''
    Writes the list to file.
    '''
    Exporter.export(wordlist,"__"+str(count)+"__"+name+".txt")
        
def findNextNomen(liste,tabu):
    '''
    returns the next word for the
    generation of a new link.
    '''
    data = []
    for wort in liste:
        if(len(wort)>4):
            if(wort.istitle() and wort not in tabu):
                data.append(wort)
    if(len(data)>0):
        return random.choice(data)
    else:
        return random.choice(["Automobil","Baum","Clown","Dach","Erde","Feuer","Gummi","Haus","Ingwer","Jodeln","Küche",
                              "Lampe","Marshmallow","Nadel","Ohr","Pinsel","Qualle","Rase","Strase","Urne","Volk",
                              "Winter","Xylophon","yack","Zitrone"]).lower()

def crwl_website(url):
    '''
    crawls a website.
    '''
    source = getWebsiteSource(url)
    words = extractToWordList(source)
    return words

def missionControl(rootUrl):
    '''
    Endless loop that navigates from
    Wikipedia page to another and saves
    extracted words in a txt file with
    pattern -> out<count>.txt
    '''
    url = rootUrl
    w=[]
    tabu=[]
    count = 0
    os.system("mkdir dist")
    os.chdir("dist")
    while(True):
        os.system("cls")
        print("https://de.wikipedia.org/wiki/"+str(url))
        s = getWebsiteSource("https://de.wikipedia.org/wiki/"+str(url))
        print(count)
        if(s!=None):
            count+=1
            w = extractToWordList(s)
            writeToFile(w,count,"Wikipedia"+str(url))
        tabu.append(url)
        url = findNextNomen(w,tabu)

def importWords(file):
    '''
    takes all files in directory and
    returns the content of all of them.
    '''
    return Importer.import_words(file)
    

def getPhoneticForWord(word):
    '''
    Returns the Phonetic for one word.
    '''
    url = 'http://tools.webmasterei.com/mbrolatester/text2pho.php'
    post_fields = {'foo': word.strip()}

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    url = None
    request = None
    post_fields = None
    return str(json.split("<")[0])
    
def getPhonetic(directory,out):
    '''
    This method handles the
    Phonetic crawl function.
    '''
    wordlist = importWords(directory)
    f = open(out,"a+")
    ret = []
    count = 0
    for i in wordlist:
        progressbar.printProgress(count,len(wordlist))
        count+=1
        phon = getPhoneticForWord(i)
        if(phon!="" and phon !=None):
            try:
                f.write(str(i)+" "+str(phon))
                f.write("\n")
            except:print("Failed to write ",str(i)," to file [",out,"]")
    f.close()
    return ret


def getSpellForWord(word):
    '''
    writes the given's wort spelling in
    a .wav file. With the name of the wort
    as filename.
    '''
    url = """
    http://mary.dfki.de:59125/process?INPUT_TYPE=TEXT&OUTPUT_TYPE=AUDIO&INPUT_TEXT=[[marcin]]&OUTPUT_TEXT=&effect_Volume_selected=&effect_Volume_parameters=amount%3A2.0%3B&effect_Volume_default=Default&effect_Volume_help=Help&effect_TractScaler_selected=&effect_TractScaler_parameters=amount%3A1.5%3B&effect_TractScaler_default=Default&effect_TractScaler_help=Help&effect_F0Scale_selected=&effect_F0Scale_parameters=f0Scale%3A2.0%3B&effect_F0Scale_default=Default&effect_F0Scale_help=Help&effect_F0Add_selected=&effect_F0Add_parameters=f0Add%3A50.0%3B&effect_F0Add_default=Default&effect_F0Add_help=Help&effect_Rate_selected=&effect_Rate_parameters=durScale%3A1.5%3B&effect_Rate_default=Default&effect_Rate_help=Help&effect_Robot_selected=&effect_Robot_parameters=amount%3A100.0%3B&effect_Robot_default=Default&effect_Robot_help=Help&effect_Whisper_selected=&effect_Whisper_parameters=amount%3A100.0%3B&effect_Whisper_default=Default&effect_Whisper_help=Help&effect_Stadium_selected=&effect_Stadium_parameters=amount%3A100.0&effect_Stadium_default=Default&effect_Stadium_help=Help&effect_Chorus_selected=&effect_Chorus_parameters=delay1%3A466%3Bamp1%3A0.54%3Bdelay2%3A600%3Bamp2%3A-0.10%3Bdelay3%3A250%3Bamp3%3A0.30&effect_Chorus_default=Default&effect_Chorus_help=Help&effect_FIRFilter_selected=&effect_FIRFilter_parameters=type%3A3%3Bfc1%3A500.0%3Bfc2%3A2000.0&effect_FIRFilter_default=Default&effect_FIRFilter_help=Help&effect_JetPilot_selected=&effect_JetPilot_parameters=&effect_JetPilot_default=Default&effect_JetPilot_help=Help&HELP_TEXT=&exampleTexts=&VOICE_SELECTIONS=bits3%20de%20male%20unitselection%20general&AUDIO_OUT=WAVE_FILE&LOCALE=de&VOICE=bits3&AUDIO=WAVE_FILE
    """.replace("[[marcin]]",word)
    f = open(word+str(".wav"),"wb")
    f.write(urlopen(url).read())
    f.close()
    
    
def getSpell(directory):
    '''
    Iterates thorught the wordlist and
    saves it on hd.
    '''
    wordlist = importWords(directory)
    for i in wordlist:
        try:
            print(i)
            getSpellForWord(i.strip())
        except:
            print("fail")

def extractBookToWordlist(pfad,count):
    """
    Extracts the content of a book to wordlist.
    Saves it with utf-8 encoding.
    <txt file>.
    """
    print(count)
    file = open(pfad,encoding='utf-8')
    text = file.read()
    file.close()
    torepl = "?=-_.,;:£!*#/*-+()[]{}123454657879809\"\'`<>\\"
    for i in torepl:
        text = text.replace(i,"")
    text = text.replace("\n"," ")
    text = text.replace("\t"," ")
    words = text.split(" ")
    words = remove_duplicates(words)
    outfile = open("out"+str(count)+".txt","a",encoding='utf-8')
    words = sorted(words)
    for i in words:
        if(i!="" and i!=None and i!="\n"):
            outfile.write(i.lower().strip())
            outfile.write("\n")
    outfile.close()


def extractBooks(pfad):
    '''
    Extracts a directory of books
    '''
    os.chdir(os.getcwd()+"\\"+str(pfad))
    i=0
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            extractBookToWordlist(file,i)
            print("Extracting:>",file)
            i+=1

def getDefinitionOfWord(word):
    '''
    gets de definition of the word from wikipedia
    '''
    s = getWebsiteSource("https://de.wikipedia.org/wiki/"+str(word))
    s = str(s).split('<p>')
    definition = removeTrash(s[1].split('</p>')[0])
    return definition



def main(argv):
    '''
    Entry Point of this module.
    Supports three functions.
    Word Crawling
    Phonetic Crawling ->Dir as argument
    Spell crawling ->Dir as argument
    '''
    if(sys.argv[1]=="crawl_words"):
        print("internet word crawl mode")
        missionControl("Null")
    elif(sys.argv[1]=="crawl_phonetic"):
        print("phonetic crawl mode")
        directory = sys.argv[2]
        getPhonetic(sys.argv[3])
    elif(sys.argv[1]=="crawl_spelling"):
        print("Synthesizer crawl mode")
        directory = sys.argv[2]
        getSpell(sys.argv[3])
    elif(sys.argv[1]=="crawl_books"):
        print("book crawl mode")
        extractBooks(sys.argv[2])

if __name__ == "__main__":
    try:
        main(sys.argv)
    except:
        print("Wrong Arguments")
