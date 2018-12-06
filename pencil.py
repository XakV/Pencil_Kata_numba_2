'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''
import re

class Pencil():

    upper_case_wear = 2
    lower_case_wear = 1
    other_printable_wear = 1
    space_or_non_printing_wear = 0

    def __init__(self,pencil_id="default",point_durability=0, length=10, eraser_durability=0):
        self.point_durability = point_durability
        self.pencil_id = pencil_id
        self.starting_durability = point_durability
        self.length = length
        self.eraser_durability = eraser_durability
        if self.length > 0:
            self.too_small_to_sharpen = False
        elif self.length == 0:
            self.too_small_to_sharpen = True
        else:
            raise Exception("A pencil can not have a length < 0")

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
        if self.too_small_to_sharpen == False:
            self.point_durability = self.starting_durability
            self.length = self.length - 1
        else:
            self.length = 0
            self.too_small_to_sharpen = True
        return self

    def erase(self, text, characters_to_remove):
        erasing_list = []
        for erased_chars in characters_to_remove.split():
            if len(erased_chars) > self.eraser_durability:
                erased_chars = erased_chars[:self.eraser_durability]
                erasing_list.append(erased_chars)
                self.eraser_durability = self.eraser_durability - len(erased_chars)
            else:
                self.eraser_durability = self.eraser_durability - len(erased_chars)
                erasing_list.append(erased_chars)
        assemble_erase_string = ''
        for word in erasing_list:
            assemble_erase_string = assemble_erase_string + word + ' '
        final_erase_string = assemble_erase_string.rstrip()
        for erase_match in re.finditer(final_erase_string, text):
            pass    #erase_match gives an re object containing the last match
        begin_text_erase = erase_match.span()[0]
        end_text_erase = erase_match.span()[1]
        erased_text = text[:begin_text_erase] + text[end_text_erase:]
        #erased_text = text[begin_text_erase:] + text[:end_text_erase]
        print(text[begin_text_erase:])
        print(text[:begin_text_erase])
        print(text[end_text_erase:])
        print(text[:end_text_erase])
        '''
        I know this needs some explanation and if I am
        explaining, there is a better way.
        ----------------------------
        re.finditer gives me an object
        of the last match. the object has a tuple of the start and
        end indices of the match. I am using the values in the tuple
        to create a string slice below.
        '''
        return self, erased_text
