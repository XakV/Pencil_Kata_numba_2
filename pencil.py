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


def write_text_with_pencil(paper_file=None, new_text_to_add=None, pencil=None):
    if pencil is None:
        pencil = pencil.create_new_pencil()
    current_pencil = pencil
    if new_text_to_add is None:
        new_text_to_add = ''
    if paper_file is None:
        raise Exception("Paper is needed to begin writing")
    p_durability = current_pencil['durability']
    text_as_written = ''
    for character in new_text_to_add:
        if p_durability > 0:
            if character.isspace() == True:
                continue
            elif character.isupper() == True:
                p_durability -= 2
            elif character.islower() == True or character.isprintable() == True:
                p_durability -= 1
            else:
                continue
            text_as_written = text_as_written.join(character)
        elif p_durability == 0:
            text_as_written = text_as_written + (' ')
        else:
            print('Unexpected pencil durability')
    current_pencil['durability'] = p_durability
    commit_to_paper = paper.record_text_on_paper(paper_file, text_as_written)
    return commit_to_paper, current_pencil
