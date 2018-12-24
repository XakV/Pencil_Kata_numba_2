import subprocess
from subprocess import PIPE
import click
from pencil import *
import io


def test_calling_the_pencil_executable_runs_the_program():
    call_pencil_cli = subprocess.Popen(['./pencil_cli.py'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    pencil_input = io.TextIOWrapper(call_pencil_cli.stdin, encoding='UTF-8', line_buffering=True)
    pencil_input.write('X')
    output_of_call = call_pencil_cli.communicate()[0].decode('utf-8')
    assert output_of_call == 0


def test_the_program_parses_the_help_option():
    pencil_cli_help_output = subprocess.call(['./pencil_cli.py', '--help'], shell=False)
    assert pencil_cli_help_output == 0
