#!/usr/bin/env python3

import paper
import click





def replace_chardict_with_char_list(edited_dict):
    new_char_list = []
    for first_char, second_char in edited_dict:
        if first_char.isprintable() and not str(first_char).isspace():
            new_char_list.append('@')
        else:
            new_char_list.append(second_char)
    return new_char_list


class WritingTool:
    lower_case_character_wear = 1
    upper_case_character_wear = 1
    other_printable_char_wear = 1

    def __init__(self, durability=None):
        self.durability = durability

    def degrade_writing_tool(self, character):
        if character.isupper():
            self.durability -= self.upper_case_character_wear
        elif character.islower():
            self.durability -= self.lower_case_character_wear
        elif character.isprintable() and not character.isspace():
            self.durability -= self.other_printable_char_wear
        elif character.isspace():
            self.durability -= 0
        else:
            raise Exception("Unexpected Character Found")
        return self


class Eraser(WritingTool):
    def __init__(self, durability=0):
        WritingTool.__init__(self, durability)
        self.eraser_durability = durability

    def erase(self, filename, string_to_erase):
        erased_string = ''
        for character in string_to_erase:
            self.degrade_writing_tool(character)
            if self.durability < 0:
                character = character
                self.durability = 0
            else:
                character = ' '
            erased_string += character
        opened_file = paper.open_file(filename)
        file_text, erase_location = paper.find_text_in_file(opened_file, string_to_erase)
        string_before_erase = file_text[:erase_location]
        len_of_erase = len(string_to_erase)
        original_string_len = len(file_text)
        if len_of_erase + erase_location >= original_string_len:
            string_after_erase = string_before_erase + erased_string
        else:
            string_after_erase = string_before_erase + erased_string + file_text[(erase_location + len_of_erase):]
        erased_file = paper.put_text(opened_file, string_after_erase)
        return erased_file


class Pencil(WritingTool):
    def __init__(self, durability=0, length=None):
        WritingTool.__init__(self, durability)
        self.length = length
        self.upper_case_character_wear = 2
        self.starting_durability = self.durability

    def write_text(self, filename, text_to_write=None):
        parsed_text = ''
        for character in text_to_write:
            self.degrade_writing_tool(character)
            if self.durability < 0:
                character = ' '
                self.durability = 0
            else:
                character = character
            parsed_text = parsed_text + character
        existing_file = paper.open_file(filename)
        with open(existing_file, 'r+') as text_file:
            existing_text = text_file.read()
        if existing_text is not None:
            written_text = existing_text + parsed_text
        else:
            written_text = parsed_text
        with open(existing_file, 'w') as write_to_file:
            write_to_file.write(written_text)
        return existing_file

    def sharpen(self):
        if self.length <= 0:
            print("Can't sharpen this pencil. It is too short.")
        else:
            self.length -= 1
            self.durability = self.starting_durability
            print("Pencil sharpened. New durability is {}".format(self.durability))
            print("Resulting pencil length is now {}".format(self.length))
        return self


class PencilAndEraser(Pencil, Eraser):
    def __init__(self, pencil_durability=0, length=0, eraser_durability=0):
        Pencil.__init__(self, pencil_durability, length)
        Eraser.__init__(self, eraser_durability)
        WritingTool.__init__(self, durability=pencil_durability)
        self.eraser_durability = eraser_durability

    def edit(self, filename, word_to_erase, replacement_text):
        with open(filename, 'r') as file_to_edit:
            existing_text = file_to_edit.read()
        if existing_text is not None:
            begin_replace = paper.find_text_in_file(filename, word_to_erase)
        replacement_file = paper.open_file(filename)
        written_replacement_text = self.write_text(replacement_file)
        phrase_to_edit = existing_text[begin_replace:]
        remainder_text = existing_text[(begin_replace + len(replacement_text)):]
        edit_dict = zip(list(phrase_to_edit), list(written_replacement_text))
        complete_edited_string = ''.join(replace_chardict_with_char_list(edit_dict))
        start_phrase = initial_text[:begin_replace]
        if len(start_phrase) + len(complete_edited_string) >= len(initial_text):
            edited_text = start_phrase + complete_edited_string
        else:
            edited_text = start_phrase + complete_edited_string + remainder_text
        filename = paper.put_text(filename, edited_text)
        return filename
