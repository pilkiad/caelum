"""
> Entry point for funl

Greetings, traveler!
You have reached the entry point for funl - the silly functional programming
language.

This module is the first that is being called when funl is run, it is
essentially just responsible for calling the other modules.
"""

# TODO - add line where error happened to output
# TODO - add more comments

import sys
sys.setrecursionlimit(50000)

from . import parser
from . import interpreter
from .utils import grammar
from .utils import logger

# TODO - add argparse -d
logger.enable_debug = False

model = parser.file_to_model("examples/import.clm", grammar.grammar)
interpreter.interpret_model(model)

print("")
