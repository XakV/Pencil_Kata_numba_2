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


def draw_user_interface(action, current_paper):
    pretty_action = action[0].upper() + action[0:]
    click.echo()
    click.echo("=============================================")
    click.echo("{} text on paper {}".format(pretty_action, current_paper))
    click.echo("=============================================")
    click.echo("Enter text to {} with pencil: ".format(action))
    click.echo()
    text_to_action = click.get_text_stream('stdin')
    return text_to_action

def action(selection, current_pencil, current_paper):
    if not current_pencil:
        current_pencil = create_a_pencil()
    if not current_paper:
        current_paper = create_or_select_paper()
    with open(current_paper, 'r') as read_paper:
        text = read_paper.read()
    click.echo("Text in current file is: ")
    click.echo()
    click.echo(text)
    if selection == 'write':
        text_to_write = draw_user_interface(action, current_paper)
        current_pencil = current_pencil.write_text(text, text_to_write)
    elif selection == 'erase':
        text_to_erase = draw_user_interface(action, current_paper)
        if text_to_erase in text:
            current_pencil = current_pencil.erase(current_paper, text, text_to_erase)
        else:
            print("Your selection does not exist in the current paper.")
    elif selection == 'edit':
        text_to_edit = draw_user_interface(action, current_paper)
        click.echo("Enter text to replace with pencil: ")
        click.echo()
        text_to_replace = click.get_text_stream('stdin')
        if text_to_edit in text:
            current_pencil = current_pencil.edit(current_paper, text_to_edit, text_to_replace)
        else:
            print("Your selection does not exist in the current_paper.")
    elif selection == 'show_stats':
        show_stats(current_pencil)
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


@click.command()
def create_a_pencil():
    pencil_id = None
    while pencil_id is None:
        click.echo("Creating New Pencil and Eraser")
        click.echo("==============================")
        click.echo()
        click.echo("Give this pencil an identifier (name): ")
        pencil_id = click.get_text_stream('stdin')
        click.echo("Assign pencil durability: ")
        pencil_durability = click.get_text_stream('stdin')
        click.echo("Length of pencil: ")
        pencil_length = click.get_text_stream('stdin')
        click.echo("Assign Eraser Durability: ")
        eraser_durability = click.get_text_stream('stdin')
        click.echo("{} pencil will be created with {} durability, {} eraser durability, and {} length.".format(pencil_id, pencil_durability, eraser_durability, pencil_length))
        proceed = click.getchar("Is this correct? Y/n")
        if proceed in ["Y", "y"]:
            pencil_id = PencilAndEraser(pencil_durability, pencil_length, eraser_durability)
    return pencil_id


@click.command()
def create_or_select_paper():
    current_paper = None
    while paper_id is None:
        click.echo("Creating or Select Paper file")
        click.echo("==============================")
        click.echo()
        click.echo("Find existing paper? (Y/n): ")
        open_paper = click.getchar()
        if open_paper in ['Y', 'y']:
            click.echo("Please type the name of the paper file: ")
        else:
            click.echo("Please type a name for the paper file: ")
        paper_name = click.get_text_stream('stdin')
        current_paper = paper.find_file(paper_name)
        if current_paper != paper_name:
            print("Something went wrong, created a new paper named {}".format(current_paper))
    return current_paper


@click.command()
def show_menu():
    menu = 'main'
    current_pencil = None
    current_paper = None
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
            if selection in ['X', 'x']:
                exit(0)
            elif selection in main_menu.keys():
                menu = main_menu[selection]
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
            if selection in ['B', 'b']:
                menu = main_menu
            elif selection in text_menu.keys():
                current_pencil, current_paper = action(text_menu[selection], current_pencil, current_paper)
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
            if selection in ['B', 'b']:
                menu = main_menu
            elif selection in paper_menu.keys():
                current_pencil, current_paper = action(paper_menu[selection], current_pencil, current_paper)
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
            if selection in ['B', 'b']:
                menu = main_menu
            elif selection in ['V', 'v']:
                current_pencil = action('show_stats', current_pencil)
            else:
                click.echo('You selected {} - which is not an option. Please try again'.format(selection))
        else:
            continue


@click.command()
def main():
    """
        The pencil cli tool is a menu driven pencil simulator.
        It should be called with no arguments.
    """

    # print the banner
    banner()
    while True:
        show_menu()


if __name__ == '__main__':
    main()
