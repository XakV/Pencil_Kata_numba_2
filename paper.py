'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''

from pencil import *
from math import random


def create_a_paper(paper_file_name=None):
    if paper_file_name is None:
        paper_file_name = random(0, 100000000).tostring + ".txt"


def show_written_text(paper_file_name=None, output_destination=None):
    if paper_file_name is None:
        raise Exception("No Paper Selected, please select or create a paper file:")
        continue
    else:
        with open(paper_file_name, 'r') as paper_file:
            if output_destination == None or output_destination == "terminal":
                print([line for line in paper_file.readlines()])
            else:
                resulting_test_string = ''
                for line in paper_file.readlines()
                    resulting_test_string.append(line)
        paper_file.close()
        if output_destination not in [None, "terminal"]:
            return paper_file_name, resulting_testing_string
        else:
            return paper_file_name

def record_text_on_paper(paper_file_name=None, written_text=None):
    if paper_file_name is None:
        raise Exception("No Paper Selected, please select or create a paper file:")
        continue
    elif written_text is None:
        raise Exception("No text to write. Please write some text.")
    else:
        with open(paper_file_name, 'a') as paper_file:
            paper_file.write(write_text_with_pencil(paper_file, written_text, pencil_used))
        paper_file.close()
    return paper_file_name

