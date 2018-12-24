#!/usr/bin/env python3


from pencil import *
import paper
import click


def banner():
    print('''
             =========================================================x
            |      | | |______________________________________________  x
            |      | | |____                       ____________________    x
            |      | | |____ PENCIL SIMULATOR 3000 ___________________     | x
            |      | | |_______________________________________________    x
            |      | | |                                                x
             =========================================================x
             ''')


def action(selection, current_pencil, current_paper):
    if current_pencil is not None and current_paper is not None:
        if selection == 'write':
            current_pencil = current_pencil.write_text()
        elif selection == 'erase':
            current_pencil = current_pencil.erase()
        elif selection == 'edit':
            current_pencil = current_pencil.edit()
        elif selection == 'show_stats':
            show_stats(current_pencil)
        else:
            pass
    elif not current_pencil:
        current_pencil == create_or_select_pencil()
    elif not current_paper:
        current_paper == create_or_select_paper()
    else:
        pass
    return current_pencil, current_paper


@click.command()
def show_stats(current_pencil):
    click.clear()
    banner()
    click.echo()
    click.echo("===========================================================")
    click.echo()
    if current_pencil is not None:
        click.echo("Showing statistics for current pencil id = {}".format(current_pencil))
        click.echo("Durability of this pencil: {}".format(current_pencil.durability))
        click.echo("Length of this pencil: {}".format(current_pencil.length))
        click.echo("Durability of the eraser: {}".format(current_pencil.eraser_durability))
    else:
        click.echo("No Pencil Selected")
        pass
    return current_pencil



    pass


@click.command()
def create_or_select_pencil(current_pencil):
    pass


@click.command()
def create_or_select_paper(current_pencil):
    pass


@click.command()
def show_menu():
    current_pencil = None
    current_paper = None
    action = None
    menu = 'main'
    main_menu = {'T': 'text_menu', 't': 'text_menu',
                 'O': 'paper_menu', 'o': 'paper_menu',
                 'S': 'stats_menu', 's': 'stats_menu'}
    text_menu = {'C': 'create_pencil', 'c': 'create_pencil',
                 'W': 'write', 'w': 'write'}
    paper_menu = {'S': 'select_paper', 's': 'select_paper',
                  'E': 'erase', 'e': 'erase',
                  'C': 'edit', 'c': 'edit'}
    while True:
        if menu == 'main':
            click.echo('Pencil Simulator - Main Menu - Please make a selection')
            click.echo('====================================================')
            click.echo()
            click.echo('T - Write Text With Pencil')
            click.echo('O - Open a Saved Paper to Edit or Erase')
            click.echo('S - Show Pencil and Eraser Stats')
            click.echo('X - Exit Pencil Simulator')
            click.echo()
            click.echo('====================================================')
            selection = click.getchar()
            for select_key, option_val in main_menu:
                if selection in select_key:
                    menu = option_val
                elif selection in ['X', 'x']:
                    exit(0)
                else:
                    click.echo('You selected {} - which is not an option. Please try again'.format(selection))
        elif menu == 'text_menu':
            click.echo('Pencil Simulator - Writing Menu - Please make a selection')
            click.echo('=======================================================')
            click.echo()
            click.echo('C - Create a new Pencil')
            click.echo('W - Write text with Pencil')
            click.echo('B - Back to Main Menu')
            click.echo()
            click.echo('Using pencil {}'.format(current_pencil))
            click.echo('=======================================================')
            selection = click.getchar()
            for select_key, option_val in main_menu:
                if select_key in ['B', 'b']:
                    menu = main_menu
                if selection in select_key:
                    current_pencil, current_paper = action(option_val, current_pencil, current_paper)
                else:
                    click.echo('You selected {} - which is not an option. Please try again'.format(selection))
        elif menu == 'paper_menu':
            click.echo('Pencil Simulator - Paper Menu - Please make a selection')
            click.echo('=======================================================')
            click.echo()
            click.echo('S - Create a new or select an existing Paper')
            click.echo('E - Erase words from Current Paper')
            click.echo('C - Change or Edit text on Current Paper')
            click.echo('B - Back to Main Menu')
            click.echo()
            click.echo('Using paper {}'.format(current_paper))
            click.echo('=======================================================')
            selection = click.getchar()
            for select_key, option_val in paper_menu:
                if select_key in ['B', 'b']:
                    menu = main_menu
                elif selection in select_key:
                    current_pencil, current_paper = action(option_val, current_pencil, current_paper)
                else:
                    click.echo('You selected {} - which is not an option. Please try again'.format(selection))
        elif menu == 'stats_menu':
            click.echo('Pencil Simulator - Stats - Please make a selection')
            click.echo('=======================================================')
            click.echo()
            click.echo('V - View stats of pencil and eraser')
            click.echo('B - Back to Main Menu')
            click.echo()
            click.echo('Using pencil {}'.format(current_pencil))
            click.echo('=======================================================')
            selection = click.getchar()
            for select_key, option_val in main_menu:
                if select_key in ['B', 'b']:
                    menu = main_menu
                elif select_key in ['V', 'v']:
                    current_pencil, current_paper = action(option_val, current_pencil)
                else:
                    click.echo('You selected {} - which is not an option. Please try again'.format(selection))
        else:
            continue


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

    # print the banner
    while True:
        banner()
        selection = menu()
        print(selection)
        if selection == str(7):
            print("Thanks for using Pencil Simulator 3000")
            exit(0)


if __name__ == '__main__':
    pencil_cli()
