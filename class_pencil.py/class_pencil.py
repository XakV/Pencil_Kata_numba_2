class WritingTool:

    durability = None
    printable_character_wear = 1
    space_or_non_printable_character_wear = 0

    def __init__(self, tool_id, durability=None, can_regenerate=False):

        self.can_regenerate = can_regenerate
        self.tool_id = tool_id
        self.durability = durability

class Pencil(WritingTool):

    lower_case_character_wear = WritingTool.printable_character_wear
    upper_case_character_wear = WritingTool.printable_character_wear * 2

    def __init__(self, length=None):
        WritingTool.__init__(self)
        self.length = length
        self.point_durability = WritingTool.durability

class Eraser(WritingTool):

    def __init__(self):
        WritingTool.__init__(self)
        self.eraser_durability = WritingTool.durability

