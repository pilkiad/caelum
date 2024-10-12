"""
> funl parser

This module takes in .funl files and produces interpretable textx models that
will later be given to the interpreter.
"""

from textx import metamodel_from_str

from .utils import logger


def file_to_model(input_file_path: str, grammar: str) -> any:
    """
    Calls on textx to convert an input file into a usable textx model by
    applying a given grammar to it.

    input_file_path: str    Path to the file that should get parsed
    grammar: str            The applied textx grammar, most likely from
                            utils/grammar

    textx.Model             Resulting textx model
    """

    logger.log_debug("Logger", f"file_to_model: {input_file_path}")

    with open(input_file_path) as file:
        input_text = file.read()

    return string_to_model(input_text, grammar)


def string_to_model(input_text: str, grammar: str) -> any:
    """
    Calls on textx to convert an input string into a usable textx model by
    applying a given grammar to it.

    input_text: str     The input string, should be a funl program
    grammar: str        The applied textx grammar, most likely from utils/grammar

    textx.Model         Resulting textx model
    """

    logger.log_debug("Logger", f"string_to_model: {input_text}")

    try:
        metamodel = metamodel_from_str(grammar)
        model = metamodel.model_from_str(input_text)
    except Exception as e:
        logger.log_error("Parser", f"Could not parse input file: {e}")

    return model
