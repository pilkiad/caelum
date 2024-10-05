"""
> Interprets funl models

NOTE - currently WIP until I finally get my head around how recursive interpretation
works
"""

from .utils import logger
from .utils import globalvars

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

    if statement.__class__.__name__ == "Model":
        interpret_model(statement)
    if statement.__class__.__name__ == "FunctionCall":
        return _evaluate_function_call(statement)
    if statement.__class__.__name__ == "FunctionDefinition":
        return _evaluate_function_definition(statement)
    else:
        return statement


def _evaluate_function_call(statement: any) -> any:
    """
    TBD
    """

    logger.log_debug("Interpreter", f"_evaluate_function_call: {statement.name}")

    evaluated_params = [_evaluate_expression(param) for param in statement.params]

    try:
        function_call = FUNCTION_MAP[statement.name]
    except KeyError:
        function_call = globalvars.environment.get(statement.name)
        if function_call is not None:
            return _evaluate_expression(function_call)
        else:
            logger.log_error("Interpreter", f"Calling an unknown function: {statement.name}")

    return function_call(evaluated_params)


def _evaluate_function_definition(statement: any) -> any:
    logger.log_debug("Interpreter", f"_evaluate_function_definition: {statement.name}")
    if statement.function is not None:
        globalvars.environment.update({statement.name: statement.function})
    elif statement.code_block is not None:
        globalvars.environment.update({statement.name: statement.code_block})
    else:
        logger.log_error("Interpreter", f"Invalid function definition: {statement.name}")