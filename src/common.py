"""
Contains the general non-menu functions for the package.
"""

# Imports
import os
import colorama
from colorama import Fore, Back, Style
from termcolor import colored


def ClearScreen():
    """Clears the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def NotYet():
    ErrorPrint("\nThis function is not yet "
                "implemented. Aborting.")

def ColorMessage(message: str, fore: str = 'white'):
    """
    Wrapper for Colorize() that directly prints to console.

    :param str message: The message to colorize.
    :param str color: The color to use.
    """
    print(Colorize(message, fore))

def Colorize(message: str, fore: str = 'white'):
    """
    Colorizes a message and returns it.

    :param str message: The message to colorize.
    :param str color: The color to use.
    :return str: The colorized message.
    """
    colorama.init(autoreset=True, convert=True)
    return colored(message, fore)

def ErrorPrint(message: str):
    """
    Prints an error message to the console in red.
    
    :param str message: The message to print.
    """
    colorama.init(autoreset=True, convert=True)
    print(f"{Fore.RED}\n{message}")
