'''
Tests for Pillar Tech Pencil Kata - using pytest
Kata Specification:
 - Pencil must be able to write text on a sheet of paper
 - Paper should reflect that text is written and recorded
 - Text written by the pencil should always be appended to existing text on the paper.
'''

from pencil import Pencil
from pencil import Paper

def test_pencil_is_a_physical_object():
    """Testing instance of pencil class"""
    assert Pencil.pencil

def test_pencil_can_write():
    """Does pencil have the ability to write"""
    assert Pencil.writes

def test_paper_is_a_physical_object():
    """
    Testing instance of paper class
    Text is recorded in ASCII characters, is retreivable, and can not overwrite itself
    """
    assert Paper.paper

def test_paper_has_text():
    """
    Text is captured in ASCII format
    Text can not destroy itself
    """
    assert Paper.text

def test_paper_can_be_found():
    """
    Files in Unix-Like systems have a filename
    Files in Unix-Like systems can be found at an explicit path
    """
    assert Paper.filename
    assert Paper.filepath
