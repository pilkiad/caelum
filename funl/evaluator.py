"""
> Provides functionality for evaluating textx models

Greetings, traveler!
"""

import typing
from textx import metamodel_from_str, get_location

from funl import mm_definition as mmd
from funl.utils import eval_function as ef
from funl.utils import logger

environment: dict[str, mmd.mm["FunctionCall"]] = {}


def eval_code_block_as_model(code_block: mmd.mm["CodeBlock"]) -> None:
    """
    Turns a code block (from a defined function) into its own
    textx model so we can run the code inside the function

    code_block: mmd.mm['CodeBlock'] The code block that should be executed
    """

    assert code_block is not None

    new_model = mmd.mm.model_from_str(code_block.content)
    local_environment = {}
    eval_model(new_model, env=local_environment)

    ef.environment = None


def eval_model(
    model: mmd.mm["Model"], env: dict[str, mmd.mm["FunctionCall"]] = environment
) -> None:
    """
    Evaluates a textx model

    model: mmd.mm['Model'])                 The model to evaluate
    env: dict[str, mmd.mm['FunctionCall']]) Optional environment, used when
    calling eval_model from eval_code_block_as_model
    """

    assert model is not None

    global last_statement
    global environment

    # Either use the global env or - if one was provided - the local one
    if env != environment:
        ef.environment = env
        ef.global_environment = environment
    else:
        ef.environment = environment

    for statement in model.statement:
        logger.last_statement = statement
        eval_statement(statement, env)


def eval_statement(
    statement: str, env: dict[str, mmd.mm["FunctionCall"]] = environment
):
    """
    Evaluates a single statement within a textx model

    statement: mmd.m['Statement'] The statement to evaluate
    """

    assert statement is not None

    if isinstance(statement, mmd.mm["FunctionDefinition"]):
        if statement.function is not None:
            eval_function_definition_inbuilt(statement.name, statement.function, env)
        elif statement.code_block is not None:
            eval_function_definition_block(statement.name, statement.code_block, env)
        else:
            raise Exception("Invalid function definition")

    elif isinstance(statement, mmd.mm["FunctionCall"]):
        ef.eval_function(statement.name, statement.params)

    else:
        raise Exception("Invalid statement is neither function definition nor call")


def eval_function_definition_inbuilt(
    name: mmd.mm["ID"],
    function: mmd.mm["FunctionDefinition"],
    env: dict[str, mmd.mm["FunctionCall"]] = environment,
) -> None:
    """
    Evaluate a function definition within a textx model.
    This function was defined using an inbuilt function, i.e. a = int(0)

    name: mmd.mm['Name']                    The name of the function
    function: mmd.mm['FunctionDefinition']  The inbuilt function that was used
    """

    assert name is not None
    assert function is not None

    env.update({name: function})
    ef.eval_function(name=function.name, params=function.params)


def eval_function_definition_block(
    name: mmd.mm["ID"],
    code_block: mmd.mm["CodeBlock"],
    env: dict[str, mmd.mm["FunctionCall"]] = environment,
) -> None:
    """
    Evaluate a function definition within a textx model.
    This function was defined using a code block. i.e. a = { ... }

    name: mmd.mm['Name']            The name of the function
    code_block: mmd.mm['CodeBlock'] The code of the function
    """

    assert name is not None
    assert code_block is not None

    env.update({name: code_block})
