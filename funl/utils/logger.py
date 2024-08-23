"""
Provides functionality for simplified logging
"""

from textx import get_location
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

input_code: str = None
last_statement: str = None


def err(errtype: str, reason: str, hints: list[str] = None) -> None:
    """
    Prints an error message to the console
    SIDEEFFECT: exits the application with an error code

    errtype: str    The type of error
    reason: str     Customizable error message
    """
    # TODO - turn errtype into enum

    global last_statement
    global input_code

    # Prepare some useful information
    location = get_location(last_statement)
    line = location["line"] - 1
    file = location["filename"]
    start_pos = last_statement._tx_position
    end_pos = last_statement._tx_position_end

    print("")
    print(
        f"A {Fore.RED}critical error{Style.RESET_ALL} has occured in file "
        + f"{Style.BRIGHT}{file}{Style.RESET_ALL} on line "
        + f"{Style.BRIGHT}{line}{Style.RESET_ALL}:"
    )
    print(f"{Style.BRIGHT}{reason}{Style.RESET_ALL}")

    if line != 0:
        print(f"{Fore.LIGHTBLACK_EX}{input_code[start_pos:end_pos]}{Style.RESET_ALL}")

    if hints is not None:
        for msg in hints:
            hint(msg)

    exit(1)


def hint(msg: str) -> None:
    """
    Prints a helpful message to the console

    msg: str    The message to type
    """
    print(f"{Fore.BLUE}Hint: {Style.RESET_ALL}{msg}")


# TODO - add other logging levels, debug, info
