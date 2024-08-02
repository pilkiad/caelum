"""
Provides inbuilt print() function
"""

from funl import mm_definition
from funl.utils import eval_function as ef
from funl.utils import asserter
from funl.utils import logger


def handle(params: list[mm_definition.mm["Param"]] | None) -> int:
    """
    Prints params to the console

    params: list[mm_definition.mm['Param']] List of parameters, must be strs
    """

    if params == None or len(params) == 0:
        logger.err("INCORRECT_PARAMS", "Missing parameters for function 'print'")

    result = ""

    for param in params:
        value = param
        if isinstance(param, mm_definition.mm["Function"]):
            value = ef.eval_function(name=param.name, params=param.params)

        asserter.assert_type("print", value, str)
        print(value, end="")
        result += value

    print("")
    return result
