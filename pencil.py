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

    def pencil_point_durability(self, durability):
        pencil_point_durability = durability
        return self.pencil_point_durability

    def pencil_can_write_text(self):
        return pencil.pencil_can_write_text

    def write_text_with_pencil(self, new_text_to_add, character_limit=None, pencil_is_dull=False):
        if character_limit is not None and len(new_text_to_add) >= character_limit:
            space_substitution_string = " " * (len(new_text_to_add) - character_limit)
            pencil_is_dull = True
            self.new_text_added = new_text_to_add[:character_limit] + space_substitution_string
        else:
            self.new_text_added = new_text_to_add
        return self.new_text_added, pencil_is_dull
