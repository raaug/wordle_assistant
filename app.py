from flask import Flask, render_template, url_for, request
#from flask import session
#from flask_session import Session
import os, sys, string
import re
import datetime
from pprint import pprint
from string import Template
from slist import slist

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'F+F+[FcVuw=hOO)IgFZnU@)If'
# app.config['SESSION_PERMANENT'] = False
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)



def main():
    WORD_LENGTH = 5
    MAX_GUESSES = 6

    green_tuple = tuple()
    yellow_tuple = tuple()
    black_tuple = tuple()

    g_temp_set = set()
    y_temp_set = set()
    green_set = set()
    yellow_set = set()
    black_set = set()


    yellow = ''
    green = ''
    black = ''
    temp = ''
    raw = "r'"
    ending = "]+$"
    bs = '^[^'
    be = ']+$'
    regex_string = ''
    do_not_add_to_black = set()

    matching_items = []

    for count in range (6):
        word = input('word: ')
        code = input('code: ')


        for i in range(len(word)):
            if code[i] == 'b':
                black_tuple=(word[i], i)
                black_set.add(black_tuple)
            elif code[i] == 'y':
                yellow_tuple=(word[i], i)
                yellow_set.add(yellow_tuple)
            elif code[i] == 'g':
                green_tuple=(word[i],i)
                green_set.add(green_tuple)
        
        #print(green_set)
        #print(yellow_set)
        #print(black_set)

        for letter, position in green_set:
            do_not_add_to_black.add(letter)
            s = Template("(?=^.{$position}$letter)")
            g_temp_set.add(s.substitute(position=position, letter=letter))
        for item in g_temp_set:
            green += item

        for letter, position in yellow_set:
            do_not_add_to_black.add(letter)
            s = Template("(?=.*$letter)(?!^.{$position}$letter)")
            y_temp_set.add(s.substitute(position=position, letter=letter))
        #print(y_temp_set)
        for item in y_temp_set:
            yellow += item

        for letter, position in black_set:
            if letter not in do_not_add_to_black:
                black += letter

        regex_string = green + yellow + bs + black + ending
        
        pattern = re.compile(regex_string)

        for item in slist:
            if pattern.match(item):
                print(item)

if __name__ == "__main__":
    main()
