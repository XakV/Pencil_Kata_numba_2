class WritingTool:

    self.lower_case_character_wear = 1
    self.upper_case_character_wear = 1
    self.other_printable_char_wear = 1

    def __init__(self, tool_id, durability=None):

        self.tool_id = tool_id
        self.durability = durability



class Pencil(WritingTool):

    upper_case_character_wear = WritingTool.wear_factor * 2

    def __init__(self, length=None):
        WritingTool.__init__(self)
        self.length = length
        self.starting_point_durability = WritingTool.durability

    def write_text(self, text_to_write, paper_file):
        text_list = list(text_to_write)
        parsed_text_list = []
        for character in text_list:
            self.durability = degrade_writing_tool(self.durability, character)
            if self.durability < 0:
                character = ' '
                self.durability = 0
            else:
                character = character
            parsed_text_list.append(character)
        parsed_text = ''.join(parsed_erased_list)
        with open(paper_file, 'a') as target_file:
            target_file.write(parsed_text)
        return self, paper_file

    def sharpen(self):
        if self.length <= 0:
            print("Can't sharpen this pencil. It is too short.")
        else:
            self.length -= 1
            self.durability = self.starting_point_durability
            print("Pencil sharpened. New durability is {}".format(self.durability))
            print("Resulting pencil length is now {}".format(self.length))
        return self



class Eraser(WritingTool):


    def __init__(self):
        WritingTool.__init__(self)


    def erase(self, text_doc, string_to_erase):

        parsed_erased_list = []
        with open(text_doc, 'r') as text:
            existing_text = text.read()
        erase_list = list(string_to_erase)
        for character in erase_list:
            self.durability = degrade_writing_tool(self.durability, character)
            if self.durability < 0:
                character = character
                self.durability = 0
            else:
                character = ' '
            parsed_erased_list.append(character)
        parsed_erased_text = ''.join(parsed_erased_list)
        new_doc = existing_text.replace(string_to_erase, parsed_erased_text)
        with open(text_doc, 'w') as text:
            text.write(new_doc)
        return(self, new_doc)


class PencilWithEraser(self, Pencil, Eraser):

    def __init__(self, Pencil, Eraser):
        super().__init__()
        self.Pencil = Pencil
        self.Eraser = Eraser


def degrade_writing_tool(durability, character):

    if character.isupper():
        tool.durability -= tool.upper_case_character_wear
    elif character.islower():
        tool.durability -= tool.lower_case_character_wear
    elif character.isprintable() and not character.isspace():
        tool.durability -= tool.other_printed_char_wear
    elif character.isspace():
        tool.durability -= 0
    else:
        raise Exception("Unexpected Character Found")
    return durability
