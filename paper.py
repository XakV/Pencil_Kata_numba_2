'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''

def show_written_text(paper_file_name):
    if paper_file_name is None:
        raise Exception("No Paper Selected, please select or create a paper file:")
    else:
        resulting_test_string = ''
        with open(paper_file_name, 'r') as paper_file:
            for line in paper_file.readlines():
                resulting_test_string = resulting_test_string + line
    return resulting_test_string

def record_text_on_paper(paper_file_name, written_text):
    if paper_file_name is None:
        raise Exception("No Paper Selected, please select or create a paper file:")
    elif written_text is None:
        raise Exception("No text to write. Please write some text.")
    else:
        with open(paper_file_name, 'a') as paper_file:
            paper_file.write(written_text)
