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

def view_new_text(existing_text_on_paper, new_text_added, pencil, pencil_is_dull=False):
    text_instructed_to_be_written = existing_text_on_paper + new_text_added
    text_as_written, pencil_state = pencil.write_text_with_pencil(text_instructed_to_be_written)

    return text_as_written, pencil_state
