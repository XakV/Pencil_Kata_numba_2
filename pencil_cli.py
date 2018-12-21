#!/usr/bin/env python3


import pencil
import paper
import click


@click.command()
def pencil_cli():
    """
        The pencil cli tool can be called these modes   \n
        =============================================   \n
        "write" -   simulates writing text to paper     \n
                    lines wrap at 80 characters         \n
                    "ENTER" key adds text to buffer     \n
                    "ESC" key brings up menu options    \n
                                                        \n
        "erase" -   removes specified characters in the \n
                    active buffer(default) or when a    \n
                    a file is specified that the user is\n
                    owner or has permission, allows     \n
                    characters to be erased from the    \n
                                                        \n
        "edit"  -   writes text over a buffer of text or\n
                    specified file. Character entered is\n
                    parsed as the character if the user \n
                    selects a location which is either a\n
                    space, or extends the EOF. Editing  \n
                    over existing text produces an "@"  \n
                                                        \n
        "stats" -   prints out statistics for the active\n
                    session\'s pencil \n
                                                        \n
        "create"-   create a new pencil with or without \n
                    an eraser \n
                                                        \n
        "read"  -   prints the contents of the active   \n
                    buffer or specified file. \n
                         
                                                        \n
        "quit"  -   quits the program \n"""


if __name__ == '__main__':
    pencil_cli()
