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


def draw_user_interface(action_name, current_paper):
    pretty_action = action_name[0].upper() + action_name[0:]
    print()
    print("=============================================")
    print("{} text on paper {}".format(pretty_action, current_paper))
    print("=============================================")
    text_to_action = input("Enter text to {} with pencil: ".format(action_name))
    print()
    return text_to_action

def action(menu, selection, current_pencil, current_paper):
    if not current_pencil:
        current_pencil = create_a_pencil()
    if not current_paper:
        current_paper = create_or_select_paper()
    with open(current_paper, 'r') as read_paper:
        text = read_paper.read()
    print("Text in current file is: ")
    print()
    print(text)
    if selection == 'write':
        text_to_write = draw_user_interface(selection, current_paper)
        current_pencil = current_pencil.write_text(text, text_to_write)
        show_menu(menu, current_pencil, current_paper)
    elif selection == 'erase':
        text_to_erase = draw_user_interface(selection, current_paper)
        if text_to_erase in text:
            current_pencil = current_pencil.erase(current_paper, text, text_to_erase)
        else:
            print("Your selection does not exist in the current paper.")
        show_menu(menu, current_pencil, current_paper)
    elif selection == 'edit':
        text_to_edit = draw_user_interface(selection, current_paper)
        text_to_replace = input("Enter text to replace with pencil: ")
        if text_to_edit in text:
            current_pencil = current_pencil.edit(current_paper, text_to_edit, text_to_replace)
        else:
            print("Your selection does not exist in the current_paper.")
        show_menu(menu, current_pencil, current_paper)
    elif selection == 'show_stats':
        show_stats(current_pencil)
        show_menu(menu, current_pencil, current_paper)
    else:
        show_menu(menu, current_pencil, current_paper)
    return current_pencil, current_paper


def show_stats(current_pencil):
    banner()
    print()
    print("============================================================")
    print()
    if current_pencil is not None:
        print("Showing statistics for current pencil id = {}".format(current_pencil))
        print("Durability of this pencil: {}".format(current_pencil.durability))
        print("Length of this pencil: {}".format(current_pencil.length))
        print("Durability of the eraser: {}".format(current_pencil.eraser_durability))
    else:
        print("No Pencil Selected")
    return current_pencil


def create_a_pencil(menu='main_menu'):
    pencil_id = None
    print("Creating New Pencil and Eraser")
    print("==============================")
    print()
    pencil_id = input("Give this pencil an identifier (name): ")
    pencil_durability = input("Assign pencil durability: ")
    pencil_length = input("Length of pencil: ")
    eraser_durability = input("Assign Eraser Durability: ")
    print("{} pencil will be created with {} durability, {} eraser durability, and {} length.".format(pencil_id, pencil_durability, eraser_durability, pencil_length))
    proceed = input("Is this correct? Y/n")
    if proceed in ["Y", "y"]:
        pencil_id = PencilAndEraser(pencil_durability, pencil_length, eraser_durability)
    return pencil_id


def create_or_select_paper():
    current_paper = None
    print("Creating or Select Paper file")
    print("==============================")
    print()
    open_paper = input("Find existing paper? (Y/n): ")
    if open_paper in ['Y', 'y']:
        paper_name = input("Please type the name of the paper file: ")
    else:
        paper_name = input("Please type a name for the paper file: ")
    current_paper = paper.open_file(paper_name)
    if current_paper != paper_name:
        print("Something went wrong, created a new paper named {}".format(current_paper))
    return current_paper


def show_menu(menu='main', current_pencil=None, current_paper=None):
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
            print('Pencil Simulator - Main Menu - Please make a selection')
            print('====================================================')
            print()
            print('T - Write Text With Pencil')
            print('O - Open a Saved Paper to Edit or Erase')
            print('S - Show Pencil and Eraser Stats')
            print('X - Exit Pencil Simulator')
            print()
            print('====================================================')
            selection = input("Selection: ")
            if selection in ['X', 'x']:
                exit(0)
            elif selection in main_menu.keys():
                menu = main_menu[selection]
            else:
                print('You selected {} - which is not an option. Please try again'.format(selection))
                menu = 'main_menu'
        elif menu == 'text_menu':
            print('Pencil Simulator - Writing Menu - Please make a selection')
            print('=======================================================')
            print()
            print('C - Create a new Pencil')
            print('W - Write text with Pencil')
            print('B - Back to Main Menu')
            print()
            print('Using pencil {}'.format(current_pencil))
            print('=======================================================')
            selection = input("Selection: ")
            if selection in ['B', 'b']:
                menu = 'main_menu'
            elif selection in ['C', 'c'] or current_pencil == None:
                action(menu, text_menu[selection], current_pencil, current_paper)
                menu = 'text_menu'
            elif selection in ['W', 'w'] and current_pencil is not None:
                action(menu, text_menu[selection], current_pencil, current_paper)
            else:
                print('You selected {} - which is not an option. Please try again'.format(selection))
            menu = 'text_menu'
        elif menu == 'paper_menu':
            print('Pencil Simulator - Paper Menu - Please make a selection')
            print('=======================================================')
            print()
            print('S - Create a new or select an existing Paper')
            print('E - Erase words from Current Paper')
            print('C - Change or Edit text on Current Paper')
            print('B - Back to Main Menu')
            print()
            print('Using paper {}'.format(current_paper))
            print('=======================================================')
            selection = input("Selection: ")
            if selection in ['B', 'b']:
                menu = main_menu
            elif selection in paper_menu.keys():
                current_pencil, current_paper = action(menu, paper_menu[selection], current_pencil, current_paper)
            else:
                print('You selected {} - which is not an option. Please try again'.format(selection))
            menu = 'paper_menu'
        elif menu == 'stats_menu':
            print('Pencil Simulator - Stats - Please make a selection')
            print('=======================================================')
            print()
            print('V - View stats of pencil and eraser')
            print('B - Back to Main Menu')
            print()
            print('Using pencil {}'.format(current_pencil))
            print('=======================================================')
            selection = input("Selection: ")
            if selection in ['B', 'b']:
                menu = main_menu
            elif selection in ['V', 'v']:
                current_pencil = action(menu, 'show_stats', current_pencil)
            else:
                print('You selected {} - which is not an option. Please try again'.format(selection))
        else:
            menu = 'main_menu'
    return


@click.command()
def main():
    """
        The pencil cli tool is a menu driven pencil simulator.
        It should be called with no arguments.
    """

    # print the banner
    banner()
    while 1:
        show_menu()
        return


if __name__ == '__main__':
    main()
