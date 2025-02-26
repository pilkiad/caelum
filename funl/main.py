"""
> Entry point for funl

Greetings, traveler!
You have reached the entry point for funl - the silly functional programming
language.

This module is the first that is being called when funl is run, it is
essentially just responsible for calling the other modules.

Notable naming convention
-------------------------

Mypy does not work well with textx which is why we opted to not use it.
This means that all type declarations will not get checked and we can make up
our own ones.
For sake of simplicity we use 'textx.' as an indicator that the given argument
needs to be of a certain metaclass defined within utils/grammar. This means
that the example 'textx.Statement' refers to a textx object that corresponds
to the 'Statement' class defined in our textx grammar.
"""

# TODO - add line where error happened to output
# TODO - add more comments

from . import parser
from . import interpreter
from .utils import grammar
from .utils import logger

# TODO - add argparse -d
logger.enable_debug = False

model = parser.file_to_model("funl/examples/fibonacci.funl", grammar.grammar)
interpreter.interpret_model(model)

# FIXME - What even is this
print("")
