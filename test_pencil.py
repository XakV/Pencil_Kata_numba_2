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

from pencil import *
import paper
import subprocess


def test_when_a_writing_tool_is_created_it_has_a_value_for_durability():
    default_pencil = PencilAndEraser(100, 100, 100)
    assert default_pencil.durability == 100
    assert default_pencil.eraser_durability == 100


def test_paper_should_reflect_that_text_is_written_and_recorded():
    test_pencil = Pencil(100, 100)
    test_text = "Show me written text"
    filename = paper.open_file(paper.random_file())
    print(filename)
    filename = test_pencil.write_text(filename, test_text)
    with open(filename, 'r') as wrote:
        written_string = wrote.read()
    assert written_string == test_text


def test_text_written_by_pencil_should_always_be_appended_to_existing_text_on_paper():
    existing_text_on_paper = "She sells sea shells"
    new_text_added = " down by the sea shore."
    appending_pencil = Pencil(100, 100)
    filename = paper.open_file(paper.random_file())
    filename = appending_pencil.write_text(filename, existing_text_on_paper)
    filename = appending_pencil.write_text(filename, new_text_added)
    with open(filename, 'r') as full_text:
        read_appended_text = full_text.read()
    text_to_compare = existing_text_on_paper + new_text_added
    assert text_to_compare == read_appended_text


def test_a_pencil_writes_spaces_if_it_goes_dull():
    character_limit = 5
    spaces_pencil = Pencil(character_limit, 10)
    text_to_write = "astring"
    filename = paper.open_file(paper.random_file())
    filename = spaces_pencil.write_text(filename, text_to_write)
    test_with_space_subs = "astri  "
    with open(filename, 'r') as dull:
        dull_pencil_text = dull.read()
    assert dull_pencil_text == test_with_space_subs


def test_writing_spaces_and_newlines_should_not_degrade_the_pencil_point():
    test_no_degrade_pencil = Pencil(10, 10)
    test_spaces_newline = "        \n" #7 consecutive spaces and a newline
    filename = '/dev/null'
    _ = test_no_degrade_pencil.write_text(filename, test_spaces_newline)
    assert test_no_degrade_pencil.durability == 10


def test_writing_lowercase_letters_degrades_pencil_point_by_one():
    lower_test_pencil = Pencil(4, 10)
    lowercase_test_string = "text"
    filename = '/dev/null'
    _ = lower_test_pencil.write_text(filename, lowercase_test_string)
    assert lower_test_pencil.durability == 0


def test_writing_uppercase_letters_degrades_pencil_point_by_two():
    upper_test_pencil = Pencil(4, 10)
    uppercase_test_string = "Text"
    expected_string_returned = "Tex "
    filename = paper.open_file(paper.random_file())
    filename = upper_test_pencil.write_text(filename, uppercase_test_string)
    assert upper_test_pencil.durability == 0
    with open(filename, 'r') as upper_test:
        parsed_upper_text = upper_test.read()
    assert parsed_upper_text == expected_string_returned


def test_sharpening_a_pencil_restores_its_initial_point_durability():
    pencil_gets_dull = Pencil(5, 100)
    pencil_gets_dull.durability = 0
    sharpened_pencil = pencil_gets_dull.sharpen()
    assert sharpened_pencil.durability == 5


def test_sharpening_a_pencil_shortens_its_length_by_one():
    starting_pencil = Pencil(5, 10)
    starting_pencil.sharpen()
    assert starting_pencil.length == 9


def test_a_pencil_of_zero_length_can_not_be_sharpened():
    zero_pencil = Pencil(5, 0)
    zero_pencil.durability = 0
    zero_pencil.sharpen()
    assert zero_pencil.durability == 0
    assert zero_pencil.length == 0


def test_an_eraser_will_remove_the_last_instance_of_the_text_its_directed_to_erase():
    text = "erase the last word"
    eraser_test = PencilAndEraser(100, 100, 100)
    filename = paper.open_file(paper.random_file())
    filename = eraser_test.write_text(filename, text)
    filename = eraser_test.erase(filename, "word")
    with open(filename, 'r') as erased:
        erasered_text = erased.read()
    assert erasered_text == "erase the last     "


def test_when_a_pencil_is_created_it_can_be_given_a_value_for_eraser_durability():
    pencil_with_eraser = PencilAndEraser(10, 10, 10)
    assert pencil_with_eraser.eraser_durability == 10


def test_erasing_any_non_space_character_degrades_the_eraser_durability_by_one():
    text = "My bonnie lies over the ocean..."
    erase_text = "bonnie"
    degraded_eraser = Eraser(100)
    filename = paper.open_file(paper.random_file())
    with open(filename, 'w') as erase_write:
        erase_write.write(text)
    _ = degraded_eraser.erase(filename, erase_text)
    assert degraded_eraser.durability == 94


def test_an_eraser_with_a_durability_of_zero_can_not_erase():
    text = "My bonnie lies over the ocean..."
    erase_text = "bonnie lies over"
    zero_eraser = Eraser(0)
    filename = paper.open_file(paper.random_file())
    with open(filename, 'w') as erase_write:
        erase_write.write(text)
    filename = zero_eraser.erase(filename, erase_text)
    with open(filename, 'r') as erase_read:
        zero_erased_text = erase_read.read()
    assert zero_erased_text == text


def test_edit_write_new_text_over_erased_whitespace():
    initial_written_text = "Call in the dogs and put out the fire!"
    erase_word = "dogs"
    replace_word = "cats"
    edit_test_pencil = PencilAndEraser(100, 100, 100)
    filename = paper.open_file(paper.random_file())
    filename = edit_test_pencil.write_text(filename, initial_written_text)
    filename = edit_test_pencil.erase(filename, erase_word)
    filename = edit_test_pencil.edit(filename, erase_word, replace_word)
    with open(filename, 'r') as edited_file:
        edited_text = edited_file.read()
    assert edited_text == "Call in the cats and put out the fire!"


def test_edit_writing_new_characters_over_existing_replaces_the_existing_text_with_an_at_sign():
    initial_written_text = "Call in the dogs and put out the fire!"
    erase_word = "dogs"
    replace_word = "robot vacuum cleaners"
    edit_test_pencil = PencilAndEraser(100, 100, 100)
    filename = paper.open_file(paper.random_file())
    filename = edit_test_pencil.write_text(filename, initial_written_text)
    filename = edit_test_pencil.edit(filename, erase_word, replace_word)
    with open(filename, 'r') as edited_file:
        overwrite_text = edited_file.read()
    assert overwrite_text == "Call in the robot@@@c@@@ @@@a@@@sfire!"
