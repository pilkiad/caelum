"""
> .funl parser

This module takes in .funl files and produces interpretable textx models that
will later be given to the interpreter.
"""

from textx import metamodel_from_str    # converts input to textx model

from utils import logger                # logging


def file_to_model(input_file_path: str, grammar: str) -> textx.Model:
    """
    Calls on textx to convert an input file into a usable textx model by
    applying a given grammar to it.

    input_file_path: str    Path to the file that should get parsed
    grammar: str            The applied textx grammar, most likely from
                            utils/grammar

    textx.Model             Resulting textx model
    """

    with open(input_file_path) as file:
        input_text = file.read()
    
    return string_to_model(input_text, grammar)


def string_to_model(input_text: str, grammar: str) -> textx.Model:
    """
    Calls on textx to convert an input string into a usable textx model by
    applying a given grammar to it.

    input_text: str     The input string, should be a funl program
    grammar: str        The applied textx grammar, most likely from utils/grammar

    textx.Model         Resulting textx model
    """

    try:
        metamodel = metamodel_from_str(funl_grammar)
        model = metamodel.model_from_str(grammar, input_text)
    except:
        logger.log_error("Parser", "Could not parse input file")

    return model