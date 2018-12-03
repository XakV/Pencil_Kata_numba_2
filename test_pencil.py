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


import pytest
from pencil import *
import paper


def test_a_writer_can_use_a_pencil_to_write_text_on_a_sheet_of_paper():
    _pencil = pencil.create_new_pencil('_pencil', 100)
    assert _pencil['durability'] > 0


def test_paper_should_reflect_that_text_is_written_and_recorded():
    existing_text_on_paper = "Counting flowers on the wall, "
    test_pencil = pencil.create_new_pencil('test_pencil', 100)
    pencil_written_text, test_pencil = write_text_with_pencil(test_pencil, existing_text_on_paper)
    assert paper.show_written_text(existing_text_on_paper) == pencil_written_text


def test_text_written_by_pencil_should_always_be_appended_to_existing_text_on_paper():
    existing_text_on_paper = "She sells sea shells"
    new_text_added = " down by the sea shore."
    _pencil = pencil.create_new_pencil('_pencil', 100)
    pencil_written_text, _pencil = write_text_with_pencil(_pencil, new_text_added)
    new_paper_view, _pencil = paper.view_new_text(existing_text_on_paper, new_text_added, _pencil)
    assert paper.show_written_text(existing_text_on_paper) + pencil_written_text == new_paper_view


def test_when_a_pencil_is_created_it_has_a_value_for_point_durability():
    new_pencil = pencil.create_new_pencil('new_pencil')
    assert new_pencil['durability'] is not None


def test_a_pencil_writes_spaces_if_it_goes_dull():
    character_limit = 5
    _pencil = pencil.create_new_pencil("_pencil", character_limit)
    text_to_write = "A_String_longer_than_five"
    pencil_written_characters, _pencil = write_text_with_pencil(_pencil, text_to_write)
    if _pencil['durability'] == 0:
        assert pencil_written_characters + (" " * (len(text_to_write) - character_limit)) == text_to_write[:character_limit] + (" " * (len(text_to_write) - character_limit))
    else:
        assert len(pencil_written_characters) <= character_limit

def test_writing_spaces_and_newlines_should_not_degrade_the_pencil_point():
    test_pencil = pencil.create_new_pencil("test_pencil", 10)
    test_spaces = "       " #7 consecutive spaces
    test_newline = "\n"
    written_space_result, test_pencil = write_text_with_pencil(test_pencil, test_spaces)
    assert test_pencil['durability'] == 10
    written_newline_result, test_pencil = write_text_with_pencil(test_pencil, test_newline)
    assert test_pencil['durability'] == 10


def test_writing_lowercase_letters_degrades_pencil_point_by_one():
    lower_test_pencil = pencil.create_new_pencil("lower_test_pencil", 4)
    lowercase_test_string = "text"
    pencil_written_characters, test_pencil = write_text_with_pencil(lower_test_pencil, lowercase_test_string)
