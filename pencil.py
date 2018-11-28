'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''

class pencil():

    def __init__(self):
        pass

    def create_new_pencil(pencil_id="default", durability=0):
        new_pencil = {'pencil_id': pencil_id, 'durability': durability}
        return new_pencil

def write_text_with_pencil(pencil, new_text_to_add):
    current_pencil = pencil
    character_limit = current_pencil['durability']
    if character_limit is not None and len(new_text_to_add) >= character_limit:
        space_substitution_string = " " * (len(new_text_to_add) - character_limit)
        current_pencil['durability'] = 0
        new_text_added = new_text_to_add[:character_limit] + space_substitution_string
    else:
        new_text_added = new_text_to_add
        current_pencil['durability'] = character_limit - len(new_text_to_add)
    return new_text_added, current_pencil
