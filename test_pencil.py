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
    assert pencil.write_text_with_pencil() == True

def test_paper_should_reflect_that_text_is_written_and_recorded():
    assert paper.show_written_text() == True
