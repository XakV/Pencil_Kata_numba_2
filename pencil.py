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


class Eraser(WritingTool):


    def __init__(self,tool_id=None, eraser_durability=0):
        super().__init__(self)
        self.durability = eraser_durability

    def erase(self, filename, string_to_erase):
        erased_string = ''
        for character in string_to_erase:
            self.eraser_durability = self.degrade_writing_tool(character)
            if self.eraser_durability < 0:
                character = character
                self.eraser_durability = 0
            else:
                character = ' '
            erased_string += character
        file_to_erase = paper.find_file(paper_file)
        erased_file = paper.put_text(file_to_erase, parsed_text)
        return self, erased_file



class Pencil(WritingTool):

    def __init__(self, pencil_id, point=0, length=None):
        super().__init__(self)
        self.tool_id = pencil_id
        self.durability = point
        self.length = length
        self.upper_case_character_wear = self.upper_case_character_wear * 2
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
        file_to_write = paper.find_file(paper_file)
        written_file = paper.put_text(file_to_write, parsed_text)
        return self, written_file

    def sharpen(self):
        if self.length <= 0:
            print("Can't sharpen this pencil. It is too short.")
        else:
            self.length -= 1
            self.durability = self.starting_durability
            print("Pencil sharpened. New durability is {}".format(self.durability))
            print("Resulting pencil length is now {}".format(self.length))
        return self


class EditorTool:

    def __init__(self):
        self.pencil = Pencil
        self.eraser = Eraser

    def edit_existing_file(self, paper_file, entry_point_text, replacement_text):
        file_to_edit = paper.find_file(paper_file)
        editor_entry_point = paper.seek_text(file_to_edit, entry_point_text)
        with open(file_to_edit.file_name, 'w') as edit_file:
            edit_file.seek(file_to_edit.cursor_position)
            replacement_list = list(replacement_text)
            try:
                existing_characters_list = list(edit_file.read())
                for character_position in range(0, len(replacement_list)):
                    if existing_characters_list[character_position].isspace():
                        self.pencil = self.pencil.degrade_writing_tool(replacement_text[character_position])
                        if self.pencil.durability >= 0:
                            edit_file.write(replacement_character)
                        else:
                            edit_file.write(' ')
                            self.pencil.durability == 0
                    elif existing_characters_list[character_position].isprintable() == False:
                        raise Exception("End of Line or non-printable character encountered")
                    elif existing_characters_list[character_position].isprintable() and not existing_characters_list[character_position].isspace() == False:
                        self.pencil = self.pencil.degrade_writing_tool(replacement_text[character_position])
                        if self.pencil.durability >= 0:
                            edit_file.write("@")
                        else:
                            print("Pencil Point is dull.")
            except:
                print("Unknown error occurred trying to edit file {}".format(paper_file))
        return self, paper_file

