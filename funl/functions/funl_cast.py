"""
Provides inbuilt cast() function
"""

from funl import mm_definition as mmd
from funl.utils import eval_function as ef
from funl.utils import asserter
from funl.utils import logger

from funl import evaluator


def handle(params: list[mmd.mm["Param"]] | None) -> int:
    """
    Cast value to other type

    params: list[mmd.mm['Param']] List of parameters
        params[0]: mmd.mm['FunctionCall']
        params[1]: type
    """

    if params == None or len(params) != 2:
        logger.err("INCORRECT_PARAMS", "Missing parameters for function 'cast'")
    asserter.assert_type("cast", params[0], mmd.mm["FunctionCall"])
    asserter.assert_type("cast", params[1], str)

    if params[1] == "str":
        return str(ef.eval_function(name=params[0].name, params=params[0].params))
    elif params[1] == "int":
        return int(ef.eval_function(name=params[0].name, params=params[0].params))

    logger.err("INCORRECT_TYPE", f"Cannot cast to '{params[1]}'")
