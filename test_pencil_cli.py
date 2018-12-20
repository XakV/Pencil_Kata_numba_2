import subprocess
from subprocess import PIPE



def test_calling_the_pencil_executable_runs_the_program():
    pencil_cli_std_out = subprocess.call(['python3', 'pencil_cli.py'], shell=False)
    assert pencil_cli_std_out == 0

def test_the_program_parses_the_help_option():
    pass

def test_the_program_displays_info_when_the_info_option_is_selected():
    pass

def test_the_program_displays_options_for_write_erase_and_edit_stats():
    pass

def test_the_program_will_save_a_file_in_text_format():
    pass

def test_the_program_will_load_a_saved_file_and_display_the_contents():
    pass

def test_the_program_will_display_the_text_written_in_real_time():
    pass

def test_the_user_can_see_if_the_file_is_saved():
    pass

def test_the_user_is_presented_with_an_option_to_save_the_active_file_on_exit_or_load_new():
    pass

def test_user_can_see_stats_from_named_pencils():
    pass

def test_user_only_creates_objects_of_type_PencilAndEraser():
    pass

def test_user_can_select_text_to_edit_by_entering_a_word_or_phrase():
    pass

def test_user_gets_an_error_message_when_text_selected_fails():
    pass

def test_user_gets_an_error_message_when_selecting_an_invalid_program_option():
    pass

def test_user_can_run_tests_by_using_the_test_arg_on_the_command_line():
    pass

def test_the_program_displays_a_header_and_menu_on_startup():
    pass

def test_user_can_exit_the_program_cleanly():
    pass

def test_program_works_with_a_screen_reader():
    pass