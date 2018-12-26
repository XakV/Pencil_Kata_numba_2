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


def open_file(filename):
    if os.access(filename, 6):
        print("Accessing file: {}".format(filename))
    elif not posixpath.exists(filename):
        with open(filename, 'a') as try_file:
            try_file.write('')
    else:
        print("Could not create file, generating a random file name.")
        filename = random_file()
        print("Generated random filename is {}".format(filename))
        with open(filename, 'a') as rand_file:
            rand_file.write('')
    return filename


def find_text_in_file(filename, string_to_find):
    if os.access(filename, 6):
        with open(filename, 'r') as find_text:
            search_string = find_text.read()
        begin_string_location = search_string.rfind(string_to_find)
        if begin_string_location in [None, '', -1]:
            print("String - {} - not found".format(string_to_find))
    else:
        print("Could not access {}. Please choose another file.".format(filename))
    return begin_string_location


def put_text(filename, string_to_write=None):
    filename = open_file(filename)
    with open(filename, 'w') as text_file:
        text_file.write(string_to_write)
    return filename


def get_text(filename):
    filename = open_file(filename)
    with open(filename, 'r') as text_file:
        text = text_file.read()
    return text
