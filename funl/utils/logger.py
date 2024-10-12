"""
> Console logging

This module provides easy ways to log text with varying verbosity levels to
the console.

There are multiple levels of verbosity:
- info: information about the steps taken by the interpreter
- error: errors that occured during interpretation
- debug: information useful for debugging the interpreter itself
"""

from sys import exit  # quits the application on error
from colorama import Fore  # text foreground colors
from colorama import Style  # text styling options


enable_debug = True


def log_error(component: str, message: str, quit_application: bool = True) -> None:
    """
    Logs an error message to the console

    component: str          The module where the error happened
    message: str            The error message
    quit_application: bool  Whether or not the interpreter should exit after
                            the error message was logged
    """

    print(f"{Fore.RED}[Error] {Style.RESET_ALL}{message} ({component})")

    if quit_application:
        exit(-1)


def log_info(component: str, message: str) -> None:
    """
    Logs an info message to the console

    component: str          The module where the info happened
    message: str            The info message
    """

    print(f"{Fore.RESET}[Info] {message} ({component})")


def log_debug(component: str, message: str) -> None:
    """
    Logs a debug message to the console

    component: str          The module where the debug happened
    message: str            The debug message
    """

    if not enable_debug:
        return

    print(f"{Fore.CYAN}[Debug] {message} ({component}){Style.RESET_ALL}")
