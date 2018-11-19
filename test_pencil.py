'''
Tests for Pillar Tech Pencil Kata - using pytest
Kata Specification:
 - Pencil must be able to write text on a sheet of paper
 - Paper should reflect that text is written and recorded
 - Text written by the pencil should always be appended to existing text on the paper.
'''

import pytest
import pencil
import paper

def test_a_writer_can_use_a_pencil_to_write_text_on_a_sheet_of_paper():
    assert pencil.pencil_can_write_text()

def test_paper_should_reflect_that_text_is_written_and_recorded():
    existing_text_on_paper = "Counting flowers on the wall, "
    assert paper.show_written_text(existing_text_on_paper) == existing_text_on_paper

def test_text_written_by_pencil_should_always_be_appended_to_existing_text_on_paper():
    existing_text_on_paper = "She sells sea shells"
    new_text_added = " down by the sea shore."
    assert paper.show_written_text(existing_text_on_paper) + pencil.write_text_with_pencil(new_text_added) == "She sells sea shells down by the sea shore."
    assert paper.show_written_text(existing_text_on_paper) + pencil.write_text_with_pencil(new_text_added) == paper.view_new_text(existing_text_on_paper, new_text_added)
