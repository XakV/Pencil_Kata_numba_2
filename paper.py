'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''

from pencil import *

def show_written_text(existing_text_on_paper):
    return existing_text_on_paper

def view_new_text(existing_text_on_paper, new_text_added):
    view_new_text = existing_text_on_paper + new_text_added
    return view_new_text
