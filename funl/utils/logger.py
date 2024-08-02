"""
Provides functionality for simplified logging
"""

def err(errtype: str, reason: str) -> None:
    """
    Prints an error message to the console
    SIDEEFFECT: exits the application with an error code

    errtype: str    The type of error
    reason: str     Customizable error message
    """
    # TODO - turn errtype into enum

    print(f"ERROR.{errtype}: {reason}")
    exit(1)

# TODO - add other logging levels, debug, info
