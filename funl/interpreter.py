"""
> Interprets funl models

NOTE - currently WIP until I finally get my head around how recursive interpretation
works
"""

from .utils import logger
from .functions import f_print
from .functions import f_int
from .functions import f_add


# FUNCTION_MAP contains references to each inbuilt funl functions handler functions
# See functions/ fo all inbuilts
FUNCTION_MAP = {
    "print": f_print.handle,
    "int": f_int.handle,
    "add": f_add.handle
}


def interpret_model(model: any) -> None:
    """
    TBD
    """

    for statement in model.statement:
        logger.log_debug("Interpreter", f"interpret_model: {statement}")
        _evaluate_expression(statement)


def _evaluate_expression(statement: any) -> any:
    """
    TBD
    """

    logger.log_debug("Interpreter", f"_evaluate_expression: {statement}")

    if statement.__class__.__name__ == "FunctionCall":
        return _evaluate_function_call(statement)
    else:
        return statement


def _evaluate_function_call(statement: any) -> any:
    """
    TBD
    """

    evaluated_params = [_evaluate_expression(param) for param in statement.params]

    try:
        native_call = FUNCTION_MAP[statement.name]
    except KeyError:
        raise Exception("Custom functions not implemented yet!")

    logger.log_debug("Interpreter", f"_process_function_call: {statement.name}")

    return native_call(evaluated_params)