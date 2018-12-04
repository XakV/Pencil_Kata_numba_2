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
'''

import paper
import pencil

def test_a_writer_can_use_a_pencil_to_write_text_on_a_sheet_of_paper():
    _pencil = pencil.create_new_pencil('_pencil', 100)
    assert _pencil['durability']


def test_paper_should_reflect_that_text_is_written_and_recorded():
    test_pencil = pencil.create_new_pencil('test_pencil', 100)
    test_text = "Show me written text"
    test_paper = "test_paper_shows_text.txt"
    test_pencil = pencil.write_text_with_pencil(test_paper, test_text, test_pencil)
    test_paper_result = paper.show_written_text(test_paper)
    assert test_paper_result == test_text


def test_text_written_by_pencil_should_always_be_appended_to_existing_text_on_paper():
    existing_text_on_paper = "She sells sea shells"
    new_text_added = " down by the sea shore."
    paper_file = "test_appending_text.txt"
    _pencil = pencil.create_new_pencil('_pencil', 100)
    _ = pencil.write_text_with_pencil(paper_file, existing_text_on_paper, _pencil)
    _ = pencil.write_text_with_pencil(paper_file, new_text_added, _pencil)
    text_to_compare = existing_text_on_paper + new_text_added
    result_of_write = paper.show_written_text(paper_file)
    assert text_to_compare == result_of_write


def test_when_a_pencil_is_created_it_has_a_value_for_point_durability():
    new_pencil = pencil.create_new_pencil('new_pencil')
    assert new_pencil['durability'] is not None


def test_a_pencil_writes_spaces_if_it_goes_dull():
    character_limit = 5
    _pencil = pencil.create_new_pencil("_pencil", character_limit)
    text_to_write = "astringlongerthanfive"
    test_paper = "test_dull_pencil_writes_spaces.txt"
    _pencil = pencil.write_text_with_pencil(test_paper, text_to_write, _pencil)
    pencil_written_characters = paper.show_written_text(test_paper)
    assert pencil_written_characters == text_to_write[:character_limit] + (" " * (len(text_to_write) - character_limit))

def test_writing_spaces_and_newlines_should_not_degrade_the_pencil_point():
    test_pencil = pencil.create_new_pencil("test_pencil", 10)
    test_spaces = "       " #7 consecutive spaces
    test_newline = "\n"
    test_paper = "space_and_newlines_test.txt"
    test_pencil = pencil.write_text_with_pencil(test_paper, test_spaces, test_pencil)
    assert test_pencil['durability'] == 10
    test_pencil = paper.write_text_with_pencil(test_paper, test_newline, test_pencil)
    assert test_pencil['durability'] == 10


def test_writing_lowercase_letters_degrades_pencil_point_by_one():
    lower_test_pencil = pencil.create_new_pencil("lower_test_pencil", 4)
    lowercase_test_string = "text"
    expected_string_returned = lowercase_test_string
    lower_test_pencil = pencil.write_text_with_pencil("lower_test_file.txt", lowercase_test_string, lower_test_pencil)
    lower_test_result_string = paper.show_written_text("lower_test_file.txt")
    assert lower_test_result_string == lowercase_test_string

def test_writing_uppercase_letters_degrades_pencil_point_by_two():
    upper_test_pencil = pencil.create_new_pencil("upper_test_pencil", 4)
    uppercase_test_string = "Text"
    expected_string_returned = "Tex "
    upper_test_pencil = pencil.write_text_with_pencil("uppercase_test_file.txt", uppercase_test_string, upper_test_pencil)
    pencil_written_characters = paper.show_written_text("uppercase_test_file.txt")
    assert expected_string_returned == pencil_written_characters
