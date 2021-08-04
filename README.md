# Text Menu Generator

This package can be used to both colorize text and to create text menus for console applications.

## TextMenu()

TextMenu() is used to generate a text menu with or without an exit option. It returns the selection to the calling function.

**syntax:** *menus.TextMenu(<exitOpt: bool>, <option1: str>...<optionN: str>)*

## ActionMenu()

ActionMenu() is similar to TextMenu, but instead of strings, accepts tuples containing the menu item and the command to execute if the item is selected. It does not return the selection but instead executes an function.

**syntax:** *menus.TextMenu(<exitOpt: bool>, (<option1Item: str>, <option1Action: str>)...<optionNItem: str>, <optionNAction: str>))*

## EndMenu()

EndMenu() is similar to TextMenu but the options are preprogrammed. It accepts two arguments, one for the "previous" menu and one for the top-level menu of the program.

**syntax:** *menus.TextMenu(<func: str>, <topmenu: str>)*
