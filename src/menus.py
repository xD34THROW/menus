"""
Contains the menu functions for the package.
"""
# Imports
from .common import *
import colorama
from colorama import Fore, Back, Style
from termcolor import colored

def ActionMenu(exitOpt: bool = False, *options: tuple):
    """
    Prints a menu to the command line and returns the choice
    to the calling function.

    :param exitOpt: Whether to append an exit option to the menu.
    :type exitOpt: bool
    :param options: Any number of tuples for the menu options, in the
    format (menuEntry, actionFunction). The option's position in the 
    list will dictate its menu position.
    :type: tuple
    """
    # Before anything else, clear the terminal and set the color.
    os.system('color 07')
    ClearScreen()
    colorama.init(autoreset=True, convert=True)

    # First let's construct the list of menu items.
    menu = []
    choices = len(options)
    validChoice = False
    hasFailed = False
    for opt in range(0, choices):
        menu.append(f"  {opt+1}) {options[opt][0]}")
    if exitOpt:
        menu.append(f"  {opt+2}) Exit the program")

    # Now print the menu.
    print(f"Select from the following options:\n")
    for opt in menu:
        print(colored(opt,'cyan'))

    # Get the input.
    while not validChoice:
        # See if we've failed once.
        if not hasFailed:
            option = input(f"\nEnter menu selection: ")
        if hasFailed:
            ErrorPrint("Invalid selection.\nEnter menu selection: ")
            option = input()
        # Check if the input is valid.
        # First we check if it's one character long. If it's longer or
        # shorter we go back to the start.
        if len(option) != 1:
            hasFailed = True
            continue
        # If it's a character long, we make sure it's in the menu.
        if len(option) == 1:
            try:
                int(option)
            except ValueError:
                # This isn't a valid number - return to the top menu.
                hasFailed = True
                continue
            else:
                # It's an integer - now let's see if it's valid.
                if exitOpt:
                    option = int(option) - 1
                else:
                    option = int(option) - 1
                if option <= choices:
                    # It's in the menu.
                    validChoice = True
                    break
                else:
                    # Outside the bounds of the menu.
                    hasFailed = True
                    continue

    # Check if it's an exit - if not, execute the associated function.
    if exitOpt and option == len(menu) - 1:
        exit()

    cmd = options[option][1]
    if cmd[-2:] == "()":
        eval(cmd)
    else:
        eval(cmd + "()")

def TextMenu(exitOpt: bool = False, *options: str):
    """
    Prints a menu to the command line and returns the choice
    to the calling function.

    :param exitOpt: Whether to append an exit option to the menu.
    :type exitOpt: bool
    :param options: Any number of strings for the menu options.
    The option's position in the list will dictate its menu position -
    treat the menu as zero-indexed, the function compensates for that.
    :type: str
    :return: The menu choice as an integer.
    :rtype: int
    """
    # Before anything else, clear the terminal and set the color.
    os.system('color 07')
    ClearScreen()
    colorama.init(autoreset=True, convert=True)

    # First let's construct the list of menu items.
    menu = []
    choices = len(options)
    validChoice = False
    hasFailed = False
    for opt in range(0, choices):
        menu.append(f"  {opt+1}) {options[opt]}")
    if exitOpt:
        menu.append(f"  {opt+2}) Exit the program")

    # Now print the menu.
    print(f"Select from the following options:\n")
    for opt in menu:
        print(colored(opt,'cyan'))

    # Get the input.
    while not validChoice:
        # See if we've failed once.
        if not hasFailed:
            option = input(f"\nEnter menu selection: ")
        if hasFailed:
            ErrorPrint("Invalid selection.\nEnter menu selection: ")
            option = input()
        # Check if the input is valid.
        # First we check if it's one character long. If it's longer or
        # shorter we go back to the start.
        if len(option) != 1:
            hasFailed = True
            continue
        # If it's a character long, we make sure it's in the menu.
        if len(option) == 1:
            try:
                int(option)
            except ValueError:
                # This isn't a valid number - return to the top menu.
                hasFailed = True
                continue
            else:
                # It's an integer - now let's see if it's valid.
                if exitOpt:
                    option = int(option) - 1
                else:
                    option = int(option)
                
                if option <= choices:
                    # It's in the menu.
                    validChoice = True
                    break
                else:
                    # Outside the bounds of the menu.
                    hasFailed = True
                    continue

    # Check if it's an exit - if not, do the math and return the value.
    if exitOpt and option == len(menu) - 1:
        exit()
    option -= 1
    return option

def EndMenu(func: str, topmenu: str):
    """
    A variant of TextMenu() simply for exiting or continuing
    the program. If continuing the program from the calling set of 
    functions, calls the function passed to it.

    :param str func: The function to call if the user elects to
    continue.
    :param str topmenu: The function to call if the user elects to
    return to the top menu.
    """
    input("\nPress Enter to continue...")
    exit = TextMenu(False, "Continue",
                    "Return to the main menu",
                    "Exit")
    if exit == 0:
        if func[-2:] == "()":
            eval(func)
        else:
            eval(func + "()")
    elif exit == 1:
        if topmenu[-2:] == "()":
            eval(topmenu)
        else:
            eval(topmenu + "()")
    elif exit == 2:
        exit()

