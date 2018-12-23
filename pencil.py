#!/usr/bin/env python3

import paper
import click

def banner():
    print('''
             =========================================================x
            |      | | |______________________________________________  x
            |      | | |____                       ____________________    x
            |      | | |____ PENCIL SIMULATOR 3000 ___________________     | x
            |      | | |_______________________________________________    x
            |      | | |                                                x
             =========================================================x
             ''')

@click.command()
def show_menu():
    current_pencil = None
    current_paper = None
    action = None
    menu = 'main'
    main_menu = {'T': 'text_menu', 't': 'text_menu', 'O': 'paper_menu','o': 'paper_menu', 'S': 'stats_menu', 's': 'stats_menu'}
    text_menu = {'C': 'create_pencil', 'c': 'create_pencil', 'W': 'write', 'w': 'write'}
    paper_menu = {'S': 'select_paper', 's': 'select_paper', 'E': 'erase', 'e': 'erase', 'C': 'edit', 'c': 'edit'}
    while True:
        if menu == 'main':
            click.echo('Pencil Simulator - Main Menu - Please make a selection')
            click.echo('====================================================')
            click.echo()
            click.echo('T - Write Text With Pencil')
            click.echo('O - Open a Saved Paper to Edit or Erase')
            click.echo('S - Show Pencil and Eraser Stats')
            click.echo('X - Exit Pencil Simulator')
            click.echo()
            click.echo('====================================================')
            selection = click.getchar()
            for select_key, option_val in main_menu:
                if selection in select_key:
                    menu = option_val
                elif selection in ['X', 'x']:
                    exit(0)
                else:
                    click.echo('You selected {} - which is not an option. Please try again'.format(selection))
        elif menu == 'text_menu':
            click.echo('Pencil Simulator - Writing Menu - Please make a selection')
            click.echo('=======================================================')
            click.echo()
            click.echo('C - Create a new Pencil')
            click.echo('W - Write text with Pencil')
            click.echo('B - Back to Main Menu')
            click.echo()
            click.echo('Using pencil {}'.format(current_pencil))
            click.echo('=======================================================')
            selection = click.getchar()
            for select_key, option_val in main_menu:
                if select_key in ['B', 'b']:
                    menu = main_menu
                if selection in select_key:
                    action = option_val
                else:
                    click.echo('You selected {} - which is not an option. Please try again'.format(selection))
        elif menu == 'paper_menu':
            click.echo('Pencil Simulator - Paper Menu - Please make a selection')
            click.echo('=======================================================')
            click.echo()
            click.echo('S - Select an existing Paper')
            click.echo('E - Erase words from Current Paper')
            click.echo('C - Change or Edit text on Current Paper')
            click.echo('B - Back to Main Menu')
            click.echo()
            click.echo('Using paper {}'.format(current_paper))
            click.echo('=======================================================')
            selection = click.getchar()
            for select_key, option_val in paper_menu:
                if select_key in ['B', 'b']:
                    menu = main_menu
                elif selection in select_key:
                    action = option_val
                else:
                    click.echo('You selected {} - which is not an option. Please try again'.format(selection))


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

    def erase(self, original_string, substring_to_erase):
        erased_string = ''
        for character in substring_to_erase:
            self.degrade_writing_tool(character)
            if self.durability < 0:
                character = character
                self.durability = 0
            else:
                character = ' '
            erased_string += character
        erase_location = original_string.rfind(substring_to_erase)
        string_before_erase = original_string[:erase_location]
        len_of_erase = len(substring_to_erase)
        original_string_len = len(original_string)
        if len_of_erase + erase_location >= original_string_len:
            string_after_erase = string_before_erase + erased_string
        else:
            string_after_erase = string_before_erase + erased_string + original_string[(erase_location + len_of_erase):]
        return string_after_erase


class Pencil(WritingTool):
    def __init__(self, durability=0, length=None):
        WritingTool.__init__(self, durability)
        self.length = length
        self.upper_case_character_wear = 2
        self.starting_durability = self.durability

    def write_text(self, existing_text=None, text_to_write=None):
        parsed_text = ''
        for character in text_to_write:
            self.degrade_writing_tool(character)
            if self.durability < 0:
                character = ' '
                self.durability = 0
            else:
                character = character
            parsed_text = parsed_text + character
        if existing_text is not None:
            written_text = existing_text + parsed_text
        else:
            written_text = parsed_text
        return written_text


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

    def edit(self, initial_text, erased_word, erased_text, replacement_text):
        begin_replace = initial_text.rfind(erased_word)
        phrase_to_edit = erased_text[begin_replace:]
        remainder_text = initial_text[(begin_replace + len(replacement_text)):]
        written_replacement_text = self.write_text(None, replacement_text)
        edit_dict = zip(list(phrase_to_edit), list(written_replacement_text))
        complete_edited_string = ''.join(replace_chardict_with_char_list(edit_dict))
        start_phrase = initial_text[:begin_replace]
        if len(start_phrase) + len(complete_edited_string) >= len(initial_text):
            edited_text = start_phrase + complete_edited_string
        else:
            edited_text = start_phrase + complete_edited_string + remainder_text
        return edited_text

