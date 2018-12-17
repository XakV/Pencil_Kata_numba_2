import paper


class WritingTool:

    lower_case_character_wear = 1
    upper_case_character_wear = 1
    other_printable_char_wear = 1

    def __init__(self, tool_id, durability=None):
        self.tool_id = tool_id
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

    def push_changes(self, altered_text, string_to_operate_on=None, filename=None):
        filename = paper.find_file(filename)
        if string_to_operate_on:
            cursor_position = paper.seek_text(filename, string_to_operate_on=None)
            changed_file = paper.put_text(filename, altered_text, cursor_position)
        else:
            changed_file = paper.put_text(filename, altered_text)
        return filename


class Eraser(WritingTool):
    def __init__(self,tool_id=None, durability=0):
        WritingTool.__init__(self, tool_id, durability)
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
        erased_file = self.push_changes(erased_string, string_to_erase, filename)
        return self, erased_file


class Pencil(WritingTool):
    def __init__(self, tool_id, durability=0, length=None):
        WritingTool.__init__(self, tool_id, durability)
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
        written_file = self.push_changes(parsed_text, paper_file)
        return self, written_file

    def edit_existing_file(self, paper_file, entry_point_text, replacement_text):
        file_to_edit = paper.find_file(paper_file)
        editor_entry_point = paper.seek_text(file_to_edit, entry_point_text)
        with open(file_to_edit, 'w+') as edit_file:
            edit_file.seek(editor_entry_point, 0)
            editing_string = edit_file.read()
            edit_index = 0
            parsed_replacement_text = ''
            while self.durability >= 0 and edit_index < len(editing_string):
                for character in replacement_text:
                    self.degrade_writing_tool(replacement_text)
                    if editing_string[edit_index].isspace():
                        parsed_replacement_text += character
                    elif editing_string[edit_index].isprintable():
                        parsed_replacement_text += '@'
                    edit_index += 1
            file_to_edit = self.push_changes(parsed_replacement_text, entry_point_text, file_to_edit)
        if self.durability > 0 and edit_index >= len(editing_string):
            file_to_edit = self.write_text(replacement_text[:edit_index], file_to_edit)
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
    def __init__(self, pencil_id=None, pencil_durability=0, length=0, eraser_id=None, eraser_durability=0):
        Pencil.__init__(self, pencil_id, pencil_durability, length)
        Eraser.__init__(self, eraser_id, eraser_durability)
        self.eraser_durability = eraser_durability
