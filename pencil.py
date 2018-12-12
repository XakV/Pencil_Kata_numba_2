class WritingTool:

    lower_case_character_wear = 1
    upper_case_character_wear = 1
    other_printable_char_wear = 1

    def __init__(self, tool_id, durability=None):

        self.tool_id = tool_id
        self.durability = durability




class Pencil(WritingTool):

    def __init__(self, tool_id, durability=0, length=None):
        super().__init__(self)
        self.tool_id = tool_id
        self.durability = durability
        self.length = length
        self.upper_case_character_wear = self.upper_case_character_wear * 2
        self.starting_durability = self.durability

    def write_text(self, text_to_write, paper_file):
        text_list = list(text_to_write)
        parsed_text_list = []
        for character in text_list:
            self = degrade_writing_tool(self, character)
            if self.durability < 0:
                character = ' '
                self.durability = 0
            else:
                character = character
            parsed_text_list.append(character)
        parsed_text = ''.join(parsed_text_list)
        with open(paper_file, 'a') as target_file:
            target_file.write(parsed_text)
        return self, paper_file

    def sharpen(self):
        if self.length <= 0:
            print("Can't sharpen this pencil. It is too short.")
        else:
            self.length -= 1
            self.durability = self.starting_durability
            print("Pencil sharpened. New durability is {}".format(self.durability))
            print("Resulting pencil length is now {}".format(self.length))
        return self



class Eraser(WritingTool):

#TODO - this doesnt look for the last instance - it's only part of the solution

    def erase(self, text_doc, string_to_erase):

        parsed_erased_list = []
        with open(text_doc, 'r') as text:
            existing_text = text.read()
        erase_list = list(string_to_erase)
        for character in erase_list:
            self = degrade_writing_tool(self, character)
            if self.durability < 0:
                character = character
                self.durability = 0
            else:
                character = ' '
            parsed_erased_list.append(character)
        parsed_erased_text = ''.join(parsed_erased_list)
        with open(text_doc, 'r') as tdoc:
            old_text = tdoc.read()
        new_text = old_text.replace(string_to_erase, parsed_erased_text)
        with open(text_doc, 'w') as erased_file:
            erased_file.write(new_text)
        return(self, text_doc)


class PencilWithEraser(Pencil, Eraser):

    def __init__(self, pencil_name, pencil_durability, pencil_length, eraser_name, eraser_durability):
        Pencil.__init__(self, tool_id=pencil_name, durability=pencil_durability, length=0)
        Eraser.__init__(self, tool_id=None)
        self.tool_id = eraser_name
        self.eraser_durability = eraser_durability

    def edit_text(self, doc_to_edit, replacement_text):
        parsed_text_edit = []
        with open(doc_to_edit, 'w') as editing_doc:
            start_of_edit = editing_doc.seek(doct_to_edit.cursor_space)
            for character in replacement_text:
                if editing_doc.read().startswith(' '):
                    with open("/dev/null", 'w') as devnull:
                        PencilWithEraser.write_text(self, character, devnull)
                    editing_doc.write(character)
                else:
                    with open("/dev/null", 'w') as devnull:
                        PencilWithEraser.write_text(self, '@', devnull)
                    editing_doc.write('@')
        return(self, editing_doc)


def degrade_writing_tool(writing_tool, character):

    if character.isupper():
        writing_tool.durability -= writing_tool.upper_case_character_wear
    elif character.islower():
        writing_tool.durability -= writing_tool.lower_case_character_wear
    elif character.isprintable() and not character.isspace():
        writing_tool.durability -= writing_tool.other_printable_char_wear
    elif character.isspace():
        writing_tool.durability -= 0
    else:
        raise Exception("Unexpected Character Found")
    return writing_tool
