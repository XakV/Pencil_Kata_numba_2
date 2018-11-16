'''
Tests for Pillar Tech Pencil Kata - using pytest
Kata Specification:
 - Pencil must be able to write text on a sheet of paper
 - Paper should reflect that text is written
 - Text written by the pencil should always be appended to existing text on the paper.
'''

from pencil import Pencil
from pencil import Paper

# Tests for Pencil Specs
def test_pencil():
    assert Pencil.pencil
    assert Pencil.writes

# Tests for Paper Specs
def test_paper():
    assert Paper.paper
    assert Paper.text
