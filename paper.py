'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''
import posixpath
import os
import tempfile


class Paper:

    def __init__(self, cursor_position):
        self.cursor_position = 0

    def create_or_find_file(self):
        if os.access(self, 6):
            print("Accessing file: {}".format(self))
        elif not posixpath.exists(self):
            print("File Not Found or Unavailable")
            open_temp_file = input("Use Temporary File - Y/n")
            if open_temp_file == "Y":
                with open(tempfile.TemporaryFile, 'w') as temp_file_handle:
                    self = temp_file_handle
                    self.cursor_position = 0
                print("Created Temporary File")
            else:
                raise Exception("Must have a file to write, erase, or edit.")
        else:
            print("Created new file named {}".format(self))
            with open(self, 'a') as text:
                text.write()
                self.cursor_position = 0
        return self


    def seek_text(self, string_to_operate_on=None):
        paper_file = self.create_or_find_file()
        if string_to_operate_on is not None:
            with open(paper_file, 'r') as text:
                existing_text = text.read()
                try:
                    paper_file.cursor_position = existing_text.rfind(string_to_operate_on)
                except:
                    raise Exception("Text Not Found")
        else:
            print("{} was found, but is empty.".format(self))
        return paper_file

    def put_text(self, string_to_write=None):
        paper_file = self
        if string_to_write is not None:
            with open(paper_file, 'a') as text_file:
                text_file.write(string_to_write)
        else:
            raise Exception("No text written")
