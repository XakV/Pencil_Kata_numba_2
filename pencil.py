'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''
import paper

def create_new_pencil(pencil_id="default", durability=0):
        new_pencil = {'pencil_id': pencil_id, 'durability': durability}
        return new_pencil
#TODO refactor pencil degrade
def degrade_pencil_point(pencil_id="default", text_to_write=''):
    current_pencil = pencil_id
    p_durability = current_pencil['durability']
    text_as_written = ''
    for character in text_to_write:
        if p_durability >= 2:
            if character.isspace() == True or character.isprintable() != True:
                p_durability += 0
                text_as_written = text_as_written + character
                print(text_as_written)
            elif character.isupper() == True:
                p_durability -= 2
                text_as_written = text_as_written + character
                print(text_as_written)
            elif character.islower() == True:
                p_durability -= 1
                text_as_written = text_as_written + character
                print(text_as_written)
            elif character.isprintable() == True:
                p_durability -= 1
                text_as_written = text_as_written + character
                print(text_as_written)
            else:
                raise Exception("Unknown character parsed")
        elif p_durability == 1:
            if character.isupper() == True:
                p_durability = 0
                text_as_written = text_as_written + ' '
                print(text_as_written)
            elif character.islower() == True or character.isprintable() == True:
                p_durability -= 1
                text_as_written = text_as_written + character
                print(text_as_written)
            elif character.isspace() == True or character.isprintable() != True:
                p_durability += 0
                text_as_written = text_as_written + character
                print(text_as_written)
            else:
                raise Exception("Unknown character parsed")
        elif p_durability == 0:
            if character.isprintable() == True:
                text_as_written = text_as_written + ' '
            else:
                text_as_written = text_as_written + character
                print(text_as_written)
        else:
            raise Exception('Unexpected pencil durability')
    current_pencil['durability'] = p_durability
    print(text_as_written)
    return current_pencil, text_as_written

def write_text_with_pencil(paper_file=None, new_text_to_add=None, pencil=None):
    if pencil is None:
        raise Exception("Pencil is needed for writing")
    if new_text_to_add is None:
        new_text_to_add = ''
    if paper_file is None:
        raise Exception("Paper is needed to begin writing")
    current_pencil = pencil
    used_pencil, text_as_written = degrade_pencil_point(current_pencil, new_text_to_add)
    paper.record_text_on_paper(paper_file, text_as_written)
    return used_pencil
