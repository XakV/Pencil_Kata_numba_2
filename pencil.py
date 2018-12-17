import paper


def push_text(text=None, filename=None):
    filename = paper.find_file(filename)
    changed_file = paper.put_text(filename, text)
    return changed_file


def replace_text(text_replaced=None, new_text=None, filename=None):
    filename = paper.find_file(filename)
    cursor_position = paper.seek_text(filename, text_replaced)
    changed_file = paper.put_text(filename, new_text, cursor_position)
    return changed_file, cursor_position


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
        erased_file, cursor_position = replace_text(string_to_erase, erased_string, filename)
        return self, erased_file, cursor_position


class Pencil(WritingTool):
    def __init__(self, durability=0, length=None):
        WritingTool.__init__(self, durability)
        self.length = length
        self.upper_case_character_wear = 2
        self.starting_durability = self.durability

    def write_text(self, text_to_write, paper_file):
        parsed_text = ''
        for character in text_to_write:
            self.degrade_writing_tool(character)
            if self.durability < 0:
                character = ' '
                self.durability = 0
            else:
                character = character
            parsed_text = parsed_text + character
        written_file = push_text(parsed_text, paper_file)
        return self, written_file

    def edit_existing_file(self, paper_file, replacement_text, entry_point):
        file_to_edit = paper.find_file(paper_file)
        edit_index = 0
        parsed_replacement_text = ''
        with open(file_to_edit, 'r+') as edit_file:
            text_read = edit_file.read()
            editing_string = text_read[entry_point:]
            print(editing_string)
            for character in replacement_text:
                while self.durability >= 0:
                    self.degrade_writing_tool(replacement_text)
                    try:
                        print("Evaluating {} - the {}th character".format(character, edit_index))
                        print("Editing string at this index is - {}".format(editing_string[edit_index]))
                        if editing_string[edit_index].isspace():
                            parsed_replacement_text += character
                        elif editing_string[edit_index].isprintable():
                            parsed_replacement_text += '@'
                        else:
                            pass
                        edit_index += 1
                    except IndexError:
                        print("End of File, trying to append remaining text.")
            file_to_edit, cursor_position = replace_text(editing_string[:edit_index], parsed_replacement_text, file_to_edit)
        if self.durability > 0 and edit_index <= len(editing_string):
            file_to_edit = push_text(replacement_text[edit_index:], file_to_edit)
        else:
            print("Unknown error occurred or pencil dulled trying to edit file {}".format(paper_file))
        return self, file_to_edit

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
        self.eraser_durability = eraser_durability
