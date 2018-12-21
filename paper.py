#!/usr/bin/env python3

'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''
import posixpath
import os
import string
from random import randint, choice


def random_file():
    min_characters = 4
    maximum_characters = 20
    allchar = string.ascii_letters + string.digits
    random_filename = "/tmp/" + "".join(choice(allchar) for x in range(randint(min_characters, maximum_characters)))
    return random_filename


def find_file(filename):
    if os.access(filename, 6):
        print("Accessing file: {}".format(filename))
    elif not posixpath.exists(filename):
        rand_file_name = random_file()
        print("Generated random filename is {}".format(rand_file_name))
    else:
        print("Created new file named {}".format(filename))
        with open(filename, 'a') as text:
            text.write()
    return filename


def put_text(filename, string_to_write=None):
    filename = find_file(filename)
    with open(filename, 'w') as text_file:
        text_file.write(string_to_write)
    return filename

def get_text(filename):
    filename = find_file(filename)
    with open(filename, 'r') as text_file:
        text = text_file.read()
    return text
