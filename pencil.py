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


def write_text_with_pencil(paper_file=None, new_text_to_add=None, pencil=None):
    if pencil is None:
        pencil = create_new_pencil()
    current_pencil = pencil
    if new_text_to_add is None:
        new_text_to_add = ''
    if paper_file is None:
        raise Execption("Paper is needed to begin writing")
    p_durability = current_pencil['durability']
    text_as_written = ''
    for character in new_text_to_add:
        if p_durability > 0:
            if character.ascii_uppercase():
                p_durability -= 2
            elif character.ascii_printable() == True and character.ascii_whitespace != True:
                p_durability -= 1
            elif character.ascii_whitespace():
                continue
            text_as_written.append(character)
        elif p_durability == 0:
            text_as_written.append(' ')
        else:
            print('Unexpected pencil durability')
    current_pencil['durability'] = p_durability
    return text_as_written, current_pencil
