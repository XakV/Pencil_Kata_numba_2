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


def show_written_text(paper_file_name=None):
    if paper_file_name is None:
        raise Exception("No Paper Selected, please select or create a paper file:")
        continue
    else:
        with open(paper_file_name, 'a') as paper_file:
            print([line for line in paper_file.readlines()])
