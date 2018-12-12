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
        new_doc = text_doc.replace(string_to_erase, parsed_erased_text)
        return(self, new_doc)


class PencilWithEraser(Pencil, Eraser):

    def __init__(self, Pencil, Eraser):
        super().__init__()
        self.Pencil = Pencil
        self.Eraser = Eraser


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
