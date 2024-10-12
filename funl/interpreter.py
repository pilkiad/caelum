"""
> Interprets funl models

NOTE - currently WIP until I finally get my head around how recursive interpretation
works
"""

from .utils import logger
from .utils import globalvars
from .utils.function_definition import FunctionDefinition

from .functions import f_print
from .functions import f_int
from .functions import f_add
from .functions import f_in
from .functions import f_eval
from .functions import f_exit
from .functions import f_rand
from .functions import f_println


# FUNCTION_MAP contains references to each inbuilt funl functions handler functions
# See functions/ fo all inbuilts
FUNCTION_MAP = {
    "print": f_print.handle,
    "int": f_int.handle,
    "add": f_add.handle,
    "in": f_in.handle,
    "eval": f_eval.handle,
    "exit": f_exit.handle,
    "rand": f_rand.handle,
    "println": f_println.handle,
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

    logger.log_debug("Interpreter", f". _evaluate_expression: {statement}")

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

    logger.log_debug("Interpreter", f".. _evaluate_function_call: {statement.name}")

    evaluated_params = [_evaluate_expression(param) for param in statement.params]
    # TODO - think of something better than bool
    call_to_inbuilt = False

    try:
        function_call = FUNCTION_MAP[statement.name]
        call_to_inbuilt = True
    except KeyError:
        function_call = globalvars.get_function_from_name(statement.name)

    if function_call is None:
        logger.log_error(
            "Interpreter", f"Calling an unknown function: {statement.name}"
        )

    #        if function_call is not None:
    #            return _evaluate_expression(function_call)
    #        else:
    #            logger.log_error(
    #                "Interpreter", f"Calling an unknown function: {statement.name}"
    #            )

    if statement.name == "eval":
        # FIXME - does this work?
        _function_from_string(function_call(evaluated_params))
        return

    if call_to_inbuilt:
        return function_call(evaluated_params)
    elif function_call.code_block is not None:
        for i in range(0, len(function_call.params_in)):
            result = FunctionDefinition(
                name=function_call.params_in[i], params_out=evaluated_params[i]
            )
            globalvars.environment.append(result)
        return _evaluate_expression(function_call.code_block)
    elif function_call.params_out is not None:
        return function_call.params_out


def _evaluate_function_definition(statement: any) -> any:
    logger.log_debug(
        "Interpreter", f".. _evaluate_function_definition: {statement.name}"
    )

    # Case: function definition contains one function call i.e x = int()
    if statement.function is not None:
        globalvars.append_or_update(
            FunctionDefinition(
                name=statement.name, params_out=_evaluate_function_call(statement.function)
            )
        )

    # Case: function definition contains code block i.e my_func = {}
    elif statement.code_block is not None:
        globalvars.append_or_update(
            FunctionDefinition(
                name=statement.name,
                code_block=statement.code_block,
                params_in=statement.params,
            )
        )

    else:
        logger.log_error(
            "Interpreter", f"Invalid function definition: {statement.name}"
        )


def _function_from_string(name: str) -> any:
    logger.log_debug("Interpreter", f"... _function_from_string: {name}")

    function_call = globalvars.get_function_from_name(name)

    if function_call is not None and function_call.code_block is not None:
        interpret_model(function_call.code_block)
        return

    # Can't raise an error if no name was given,
    # because eval() may return None if evaluated statement is false
    if name is not None:
        logger.log_error("Interpreter", f"Tried to call invalid function: {name}")
