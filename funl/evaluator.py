"""
Provides functionality for evaluating textx models
"""

import typing
from textx import metamodel_from_str

from funl import mm_definition as mmd
from funl.utils import eval_function as ef

environment: dict[str, mmd.mm["FunctionCall"]] = {}
last_statement = None

def eval_code_block_as_model(code_block: mmd.mm["CodeBlock"]) -> None:
    new_model = mmd.mm.model_from_str(code_block.content)
    eval_model(new_model)

def eval_model(model: mmd.mm["Model"]) -> None:
    """
    Evaluates a textx model

    model: mmd.mm['Model']) The model to evaluate
    """

    assert(model is not None)

    global last_statement
    global environment

    ef.environment = environment
    for statement in model.statement:
        last_statement = statement
        eval_statement(statement)


def eval_statement(statement: str):
    """
    Evaluates a single statement within a textx model

    statement: mmd.m['Statement'] The statement to evaluate
    """

    assert(statement is not None)

    if isinstance(statement, mmd.mm["FunctionDefinition"]):
        if statement.function is not None:
            eval_function_definition_inbuilt(statement.name, statement.function)
        elif statement.code_block is not None:
            eval_function_definition_block(statement.name, statement.code_block)
        else:
            raise Exception("Invalid function definition")

    elif isinstance(statement, mmd.mm["FunctionCall"]):
        ef.eval_function(statement.name, statement.params)

    else:
        raise Exception("Invalid statement is neither function definition nor call")


def eval_function_definition_inbuilt(
    name: mmd.mm["ID"],
    function: mmd.mm["FunctionDefinition"]
) -> None:
    """
    Evaluate a function definition within a textx model.
    This function was defined using an inbuilt function, i.e. a = int(0)
    
    name: mmd.mm['Name']                    The name of the function
    function: mmd.mm['FunctionDefinition']  The inbuilt function that was used
    """

    assert(name is not None)
    assert(function is not None)

    global environment

    environment.update({name: function})
    ef.eval_function(name=function.name, params=function.params)


def eval_function_definition_block(
    name: mmd.mm["ID"],
    code_block: mmd.mm["CodeBlock"]
) -> None:
    """
    Evaluate a function definition within a textx model.
    This function was defined using a code block. i.e. a = { ... }
    
    name: mmd.mm['Name']            The name of the function
    code_block: mmd.mm['CodeBlock'] The code of the function
    """

    assert(name is not None)
    assert(code_block is not None)

    global environment

    environment.update({name: code_block})

