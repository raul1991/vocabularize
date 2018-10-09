#!/usr/bin/python
import subprocess # to help us execute os commands
import time # to help us sleep between consecutive words
from random import randrange # for random words
list_of_words=[] # list of dict of words - name, synonyms and sentence
def loadWords():
    words = open("words.txt", "r")
    for line in words.readlines():
       name,synonyms,sentence = line.split("->")
       word = {
               'name': name, 
               'synonyms': synonyms.split(","), 
               'sentence': sentence
              }
       append_word(word)


def append_word(word):
    list_of_words.append(word)


def quiz():
    total_len = len(list_of_words)
    while(True):
        notify(list_of_words[randrange(total_len)])
        time.sleep(20 * 60) # 20 minutes sleep


def display(word):
    print(word['name'])
    print(word['synonyms'])
    print(word['sentence'])


def notify(word):
    subprocess.Popen(['notify-send', '-a' , 'Recap', '--urgency=critical' , word['name'] +"\r\n", str(word['synonyms']) + "\r\n" + str(word['sentence'])])
    time.sleep(5)


loadWords()
quiz()
