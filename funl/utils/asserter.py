"""
Provides functionality for asserting datatypes and more
"""

import typing

from funl.utils import logger

def assert_type(func: str, value: typing.Any, expected: type) -> bool:
    """
    Checks if a given value is of the correct datatype and reports an error
    if that is not the case

    func: str       The inbuilt function that wants to assert the type,
                    used for error printing
    value: any      The value we want to check the type of
    expected: type  The type the variable should have

    bool:           Returns True if type is correct,
                    False otherwise
    """

    if value is None:
        logger.err("INCORRECT_TYPE",
            f"Function '{func}' expected type "
            f"'{expected.__name__}' but got "
            f"none")
        return False

    result = isinstance(value, expected)

    if not result:
        logger.err("INCORRECT_TYPE",
            f"Function '{func}' expected type "
            f"'{expected.__name__}' but got "
            f"'{type(value).__name__}'")
        return False

    return True


