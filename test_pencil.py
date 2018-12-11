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

from paper import *
from pencil import *
from random import randint

def test_when_a_writing_tool_is_created_it_has_a_value_for_durability():
    _pencil = Pencil('_pencil', 100, 100)
    _pencil.length = 100
    assert _pencil.durability == 100
    _eraser = Eraser()
    _eraser.durability = 100
    assert _eraser.durability == 100


def test_paper_should_reflect_that_text_is_written_and_recorded():
    test_pencil = Pencil('test_pencil', 100, 100)
    test_text = "Show me written text"
    test_paper = "/tmp/test_paper_shows_text" + str(randint(0, 10000))
    test_pencil, written_text = test_pencil.write_text(test_text, test_paper)
    with open(test_paper, 'r') as paper_file:
        test_paper_result = paper_file.read()
    assert test_paper_result == test_text

def test_text_written_by_pencil_should_always_be_appended_to_existing_text_on_paper():
    existing_text_on_paper = "She sells sea shells"
    new_text_added = " down by the sea shore."
    paper_file = "test_appending_text.txt" + str(randint(0, 10000))
    appending_pencil = Pencil('_pencil', 100)
    appending_pencil, paper_file = appending_pencil.write_text(existing_text_on_paper, paper_file)
    appending_pencil, paper_file = appending_pencil.write_text(new_text_added, paper_file)
    text_to_compare = existing_text_on_paper + new_text_added
    with open(paper_file, 'r') as append_paper:
        result_of_write = append_paper.read()
    assert text_to_compare == result_of_write

def test_a_pencil_writes_spaces_if_it_goes_dull():
    character_limit = 5
    spaces_pencil = Pencil("spaces_pencil", character_limit)
    text_to_write = "astring"
    spaces_pencil, spaces_file = spaces_pencil.write_text(text_to_write, "/tmp/spaces" + str(randint(0, 10000)))
    test_with_space_subs = "astri  "
    with open(spaces_file, 'r') as space_file:
        dull_pencil_text = space_file.read()
    assert dull_pencil_text == test_with_space_subs

def test_writing_spaces_and_newlines_should_not_degrade_the_pencil_point():
    test_no_degrade_pencil = Pencil("test_no_degrade_pencil", 10)
    test_spaces_newline = "        \n" #7 consecutive spaces and a newline
    create_no_degrade = "no_degrade_text" + str(randint(0, 10000))
    test_no_degrade_pencil, no_degrade_file = test_no_degrade_pencil.write_text(test_spaces_newline, create_no_degrade)
    assert test_no_degrade_pencil.durability == 10

def test_writing_lowercase_letters_degrades_pencil_point_by_one():
    lower_test_pencil = Pencil("lower_test_pencil", 4)
    lowercase_test_string = "text"
    lower_file = "/tmp/lower" + str(randint(0, 10000))
    lower_test_pencil, parsed_lowercase_file = lower_test_pencil.write_text(lowercase_test_string, lower_file)
    assert lower_test_pencil.durability == 0

def test_writing_uppercase_letters_degrades_pencil_point_by_two():
    upper_test_pencil = Pencil("upper_test_pencil", 4)
    uppercase_test_string = "Text"
    expected_string_returned = "Tex "
    upper_test_file = "/tmp/upper" + str(randint(0, 10000))
    upper_test_pencil, parsed_upper_file = upper_test_pencil.write_text(uppercase_test_string, upper_test_file)
    with open(parsed_upper_file, 'r') as parsed_upper:
        parsed_upper_return = parsed_upper.read()
    assert upper_test_pencil.durability == 0
    assert parsed_upper_return == expected_string_returned

def test_sharpening_a_pencil_restores_its_initial_point_durability():
    pencil_gets_dull = Pencil("pencil_gets_dull", 5)
    pencil_gets_dull.durability = 0
    sharpened_pencil = pencil_gets_dull.sharpen()
    assert sharpened_pencil.point_durability == 5

def test_sharpening_a_pencil_shortens_its_length_by_one():
    starting_pencil = Pencil("starting_pencil", 5)
    starting_pencil.sharpen()
    assert starting_pencil.length == 9

def test_a_pencil_of_zero_length_can_not_be_sharpened():
    zero_pencil = Pencil("zero_pencil", 5)
    zero_pencil.durability = 0
    zero_pencil.sharpen()
    assert zero_pencil.durability == 0
    assert zero_pencil.length == 0

def test_an_eraser_will_remove_the_last_instance_of_the_text_its_directed_to_erase():
    text = "erase the last word"
    _ = Pencil("default", 30)
    test_erase_file = "/tmp/eraseme" + str(randint(0,10000))
    eraser_test = Eraser("eraser_test", 100)
    _, test_erase_file = _.write_text(text, test_erase_file)
    eraser_test, test_erase_file = eraser_test.erase(test_erase_file, "word")
    with open(test_erase_file, 'r') as erase_file:
        returned_text = erase_file.read()
    assert returned_text == "erase the last "

#Need to update class to be able to add an eraser to a pencil - perhaps an EditTool class?

def test_when_a_pencil_is_created_it_can_be_given_a_value_for_eraser_durability():
    pencil_with_eraser = PencilWithEraser.Pencil("pencil_with_eraser", 10, 10)
    pencil_with_eraser = PencilWithEraser.Eraser("eraser_on_pencil", 10)
    assert pencil_with_eraser.eraser_on_pencil.durability == 10


#TODO fix all this jazz
def test_erasing_any_non_space_character_degrades_the_eraser_durability_by_one():
    text = "My bonnie lies over the ocean..."
    _pencil = Pencil("_pencil", 100)
    erased_doc = "/tmp/erased_doc"
    _pencil, erased_doc = _pencil.write_text(text, erased_doc)
    erase_text = "bonnie"
    degraded_eraser = Eraser("degraded_eraser", 100)
    degraded_eraser, returned_doc = degraded_eraser.erase(erased_doc, erase_text)
    assert degraded_eraser.durability == 96

def test_an_eraser_with_a_durability_of_zero_can_not_erase():
    text = "My bonnie lies over the ocean..."
    erase_text = "bonnie lies over"
    zero_eraser = Eraser("zero_eraser", 0)
    zero_eraser, zero_erased_file = zero_eraser.erase("/tmp/zero_erased_file", erase_text)
    with open(zero_erased_file, 'r') as unerased:
        unerased_text = unerased.read()
    assert unerased_text == text

#TODO - save these two for tomorrow
def test_edit_write_new_text_over_erased_whitespace():
    initial_written_text = "Call in the dogs and put out the fire!"
    erase_word = "dogs"
    replace_word = "cats"
    edit_test_pencil = Pencil("edit_test_pencil", 100)
    edit_test_pencil, first_write = edit_test_pencil.write_text(initial_written_text)
    edit_test_pencil, erased_text = edit_test_pencil.erase(first_write, erase_word)
    edit_test_pencil, final_text = edit_test_pencil.edit(erased_text, replace_word, start_text_position)
    assert final_text == "Call in the cats and put out the fire!"

def test_edit_writing_new_characters_over_existing_replaces_the_existing_text_with_an_at_sign():
    initial_written_text = "Call in the dogs and put out the fire!"
    erase_word = "dogs"
    replace_word = "robot vacuum cleaners"
    edit_test_pencil = Pencil("edit_test_pencil", 100)
    edit_test_pencil, first_write = edit_test_pencil.write_text(initial_written_text)
    edit_test_pencil, erased_text = edit_test_pencil.erase(first_write, erase_word)
    edit_test_pencil, final_text = edit_test_pencil.edit(erased_text, replace_word, start_text_position)
    assert final_text == "Call in the robot@@@c@@@ @@@a@@@@fire!"
