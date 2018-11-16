'''
Pencil Kata - Pillar Technology Apprentice Application
Author: Zach Villers
Started: 16 Nov 2018
Requirements: https://github.com/PillarTechnology/kata-pencil-durability
Test Framework: pytest
'''


class Pencil:
    """A Pencil is a tool for writing and drawing"""

    def pencil(self):
        """The base object of pencil"""
        return Pencil.pencil

    def writes(self):
        """A pencil that can be used for writing."""
        return Pencil.writes


class Paper:
    """Paper is the given medium for writing"""

    def paper(self):
        """Base object for paper medium"""
        return Paper.paper

    def text(self):
        """Text is created by a pencil writing on paper"""
        return Paper.text
