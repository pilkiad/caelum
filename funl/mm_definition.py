"""
Provides definition of funl grammar
"""

from textx import metamodel_from_str

funl_grammar = """
    Model: statement *= Statement;

    Statement: FunctionDefinition | Function;

    FunctionDefinition: name=ID '=' function=Function;
    Function: name=ID '(' params*=Param (',' params*=Param)* ')';

    Param: Function | INT | ID | STRING;
    Comment: /#.*$/;
    ID: /[a-zA-Z_][a-zA-Z0-9_]*/;
    INT: /[0-9]+/;
    STRING: /".*"/;
"""

# Create a metamodel from the grammar
mm = metamodel_from_str(funl_grammar)
