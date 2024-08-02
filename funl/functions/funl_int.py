"""
Provides inbuilt int() function
"""

from funl.utils import asserter
from funl.utils import logger

def handle(params: list[str]) -> int:
    """
    Represents the basic int datatype

    params: list[str]   List of parameters, must be ints
    """

    if params == None or len(params) == 0:
        logger.err("INCORRECT_PARAMS", "Missing parameters for function 'int'")
    asserter.assert_type("int", params[0], int)

    return int(params[0])

