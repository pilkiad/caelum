"""
Provides inbuilt add() function
"""

from funl import mm_definition as mmd
from funl.utils import eval_function as ef
from funl.utils import asserter
from funl.utils import logger


def handle(params: list[mmd.mm["Param"]] | None) -> int:
    """
    Adds any ints together

    params: list[mmd.mm['Param']] List of parameters, must be ints
    """

    if params == None or len(params) == 0:
        logger.err("INCORRECT_PARAMS", "Missing parameters for function 'add'")

    result = 0

    for param in params:
        value = param
        if isinstance(param, mmd.mm["FunctionCall"]):
            value = ef.eval_function(name=param.name, params=param.params)

        asserter.assert_type("add", value, int)
        result += value

    return result
