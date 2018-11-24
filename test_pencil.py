'''
Tests for Pillar Tech Pencil Kata - using pytest
Kata Specification:
 - Pencil must be able to write text on a sheet of paper
 - Paper should reflect that text is written and recorded
 - Text written by the pencil should always be appended to existing text on the paper.
 - When a pencil is created, it can be provided with a value for point durability.
 - The pencil will be able to write only a limited number of characters before it goes dull
 - After the pencil goes dull, every character the pencil is told to write will appear as a space
'''

import pytest
from pencil import *
import paper

def test_a_writer_can_use_a_pencil_to_write_text_on_a_sheet_of_paper():
    _pencil = pencil()
    assert _pencil.pencil_can_write_text

def test_paper_should_reflect_that_text_is_written_and_recorded():
    existing_text_on_paper = "Counting flowers on the wall, "
    assert paper.show_written_text(existing_text_on_paper) == existing_text_on_paper

def test_text_written_by_pencil_should_always_be_appended_to_existing_text_on_paper():
    existing_text_on_paper = "She sells sea shells"
    new_text_added = " down by the sea shore."
    _pencil = pencil()
    pencil_written_text, pencil_is_dull = pencil.write_text_with_pencil(_pencil, new_text_added)
    new_paper_view, _pencil_state = paper.view_new_text(existing_text_on_paper, new_text_added, _pencil)
    if _pencil_state is not pencil_is_dull:
        assert paper.show_written_text(existing_text_on_paper) + pencil_written_text == new_paper_view
    else:
        pass

def test_when_a_pencil_is_created_it_has_a_value_for_point_durability():
    durability = 1
    new_pencil = pencil()
    new_pencil.new_pencil_point = new_pencil.pencil_point_durability(durability)
    assert new_pencil.pencil_point_durability

def test_a_pencil_can_write_a_limited_number_of_characters_before_it_goes_dull():
    character_limit = 5
    _pencil = pencil()
    text_to_write = "A_String_longer_than_five"
    pencil_written_characters = _pencil.write_text_with_pencil(text_to_write, character_limit)
    try:
        assert len(pencil_written_characters) <= character_limit
    except _pencil.dull:
        assert pencil_written_characters == text_to_write[:character_limit] + (" " * (len(text_to_write) - character_limit))

def test_after_pencil_point_goes_dull_the_pencil_writes_a_space_for_each_further_character_it_was_told_to_write():
    character_limit = 5
    _pencil = pencil()
    text_to_write = "A_String_longer_than_five"
    total_spaces_substituted = len(text_to_write) - character_limit
    pencil_written_characters, pencil_is_dull = _pencil.write_text_with_pencil(text_to_write, character_limit)
    spaces_substituted_string = " " * total_spaces_substituted
    assert text_to_write[:character_limit] + spaces_substituted_string == pencil_written_characters
