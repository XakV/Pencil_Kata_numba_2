'''
Tests for Pillar Tech Pencil Kata - using pytest
Kata Specification:
 - Pencil must be able to write text on a sheet of paper
 - Paper should reflect that text is written
 - Text written by the pencil should always be appended to existing text on the paper.
'''

from pencil import Pencil
from pencil import Paper

def test_pencil():
    """Testing instance of pencil class and pencil's ability to write"""
    assert Pencil.pencil
    assert Pencil.writes

def test_paper():
    """Testing instance of paper class and presence of text on paper"""
    assert Paper.paper
    assert Paper.text
