'''
Tests for Pillar Tech Pencil Kata - using pytest
Kata Specification:
 - Pencil must be able to write text on a sheet of paper
 - Paper should reflect that text is written and recorded
 - Text written by the pencil should always be appended to existing text on the paper.
 - When a pencil is created, it can be provided with a value for point durability.
 - The pencil will be able to write only a limited number of characters before it goes dull
 - After the pencil goes dull, every character the pencil is told to write will appear as a space
 - Writing newlines and spaces should not degrade the pencil point
 - Writing an uppercase letter degrades the pencil point by 2
 - Writing a lowercase letter degrades the pencil point by 1
'''

from pencil import *
from paper import *


def test_when_a_pencil_is_created_it_has_a_value_for_point_durability():
    _pencil = Pencil('_pencil', 100)
    assert _pencil.point_durability == 100


def test_paper_should_reflect_that_text_is_written_and_recorded():
    test_pencil = Pencil('test_pencil', 100)
    test_text = "Show me written text"
    test_paper = "test_paper_shows_text.txt"
    test_pencil, written_text = test_pencil.parse_text_written(test_text)
    record_text_on_paper(test_paper, written_text)
    test_paper_result = show_written_text(test_paper)
    assert test_paper_result == written_text

def test_text_written_by_pencil_should_always_be_appended_to_existing_text_on_paper():
    existing_text_on_paper = "She sells sea shells"
    new_text_added = " down by the sea shore."
    paper_file = "test_appending_text.txt"
    appending_pencil = Pencil('_pencil', 100)
    appending_pencil, original_text = appending_pencil.parse_text_written(existing_text_on_paper)
    record_text_on_paper(paper_file, original_text)
    appending_pencil, new_text = appending_pencil.parse_text_written(new_text_added)
    record_text_on_paper(paper_file, new_text)
    text_to_compare = existing_text_on_paper + new_text_added
    result_of_write = show_written_text(paper_file)
    assert text_to_compare == result_of_write

def test_a_pencil_writes_spaces_if_it_goes_dull():
    character_limit = 5
    spaces_pencil = Pencil("spaces_pencil", character_limit)
    text_to_write = "astring"
    spaces_pencil, dull_pencil_text = spaces_pencil.parse_text_written(text_to_write)
    test_with_space_subs = "astri  "
    assert dull_pencil_text == test_with_space_subs

def test_writing_spaces_and_newlines_should_not_degrade_the_pencil_point():
    test_no_degrade_pencil = Pencil("test_no_degrade_pencil", 10)
    test_spaces_newline = "        \n" #7 consecutive spaces and a newline
    test_no_degrade_pencil, _ = test_no_degrade_pencil.parse_text_written((test_spaces_newline))
    assert test_no_degrade_pencil.point_durability == 10

def test_writing_lowercase_letters_degrades_pencil_point_by_one():
    lower_test_pencil = Pencil("lower_test_pencil", 4)
    lowercase_test_string = "text"
    lower_test_pencil, parsed_lowercase_text = lower_test_pencil.parse_text_written(lowercase_test_string)
    assert parsed_lowercase_text == lowercase_test_string
    assert lower_test_pencil.point_durability == 0

def test_writing_uppercase_letters_degrades_pencil_point_by_two():
    upper_test_pencil = Pencil("upper_test_pencil", 4)
    uppercase_test_string = "Text"
    expected_string_returned = "Tex "
    upper_test_pencil, parsed_upper_text = upper_test_pencil.parse_text_written(uppercase_test_string)
    assert expected_string_returned == parsed_upper_text
    assert upper_test_pencil.point_durability == 0
