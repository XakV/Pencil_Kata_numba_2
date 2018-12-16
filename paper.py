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


def seek_text(filename=None, string_to_operate_on=None):
    cursor_position = None
    if filename is not None and string_to_operate_on is not None:
        with open(filename, 'r') as text:
            existing_text = text.read()
            try:
                cursor_position = existing_text.rfind(string_to_operate_on)
            except:
                raise Exception("Text Not Found")
    else:
        print("{} was found, but is empty.".format(filename))
    return cursor_position

def put_text(filename, string_to_write=None, starting_char=None):
    if string_to_write is not None and starting_char is None:
        with open(filename, 'a') as text_file:
            text_file.write(string_to_write)
    elif string_to_write is not None and starting_char is not None:
        with open(filename, 'r+') as text_file:
            text_file.seek(starting_char, 0)
            text_file.write(string_to_write)
    else:
        raise Exception("No text written")
    return filename
