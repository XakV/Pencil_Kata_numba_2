'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''
class Pencil():

    upper_case_wear = 2
    lower_case_wear = 1
    other_printable_wear = 1
    space_or_non_printing_wear = 0

    def __init__(self,pencil_id="default",point_durability=0):
        self.point_durability = point_durability
        self.pencil_id = pencil_id
        self.starting_durability = point_durability

    def parse_text_written(self,written_characters):
        parsed_characters = ''
        for character in written_characters:
            if character.isupper():
                self.point_durability -= self.upper_case_wear
            elif character.islower():
                self.point_durability -= self.lower_case_wear
            elif character.isspace() or not character.isprintable():
                self.point_durability -= self.space_or_non_printing_wear
            elif character.isprintable() and not character.isspace():
                self.point_durability -= self.other_printable_wear
            else:
                raise Exception("Unexpected Character found")
                break
            if self.point_durability >= 0:
                parsed_characters = parsed_characters + character
            elif self.point_durability < 0:
                parsed_characters = parsed_characters + ' '
        if self.point_durability < 0:
            self.point_durability = 0
        return self, parsed_characters

    def sharpen(self):
        self.point_durability = self.starting_durability
        return self
