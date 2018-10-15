#!/usr/bin/python
import subprocess  # to help us execute os commands
import time  # to help us sleep between consecutive words
import random
import sys  # parsing args

list_of_words = []  # list of dict of words - name, synonyms and sentence


def load_words():
    del list_of_words[:]  # clearing the list
    words = open("words.txt", "r")
    for line in words.readlines():
        name, synonyms, sentence = line.split("->")
        word = {
            'name': name.lower().strip(),
            'synonyms': synonyms.split(","),
            'sentence': sentence
        }
        append_word(word)


def append_word(word):
    list_of_words.append(word)


def quiz():
    random.shuffle(list_of_words)
    for idx in list_of_words:
        notify(idx)
        time.sleep(20 * 60)  # 20 minutes sleep


def display(word):
    print(word['name'].upper())
    print(word['synonyms'])
    print(word['sentence'])


def notify(word):
    subprocess.Popen(['notify-send', '-a', 'vocabularize', '--urgency=critical', word['name'].upper() + "\r\n",
                      str(word['synonyms']) + "\r\n" + str(word['sentence'])])


def add_word():
    name = raw_input('Enter a word : ')
    if not word_exists(name):
        synonyms = raw_input('Enter the synonyms (separated by a comma): ')
        sentence = raw_input('Enter a sentence : ')
        word_file.write("%s -> %s -> %s" % (name, synonyms, sentence))
        return True
    else:
        return False

def word_exists(name):
    for w in list_of_words:
        if w.get('name') == name:
            return True


def play_quiz():
    while (True):
        quiz()


load_words()
should_add_word = (sys.argv[1] == '--add_words')
if should_add_word:
    more = 'y'
    word_file = open('words.txt', 'a+')
    while more == 'y' or more == 'yes':
        if not add_word():
            print("Word already exists")
            more = raw_input('Do you want to add more words (y/n) ?')

should_play_quiz = str(raw_input('Want to play a quiz')).strip().lower()
if should_play_quiz == 'y' or should_play_quiz == 'yes':
    load_words()
    play_quiz()
