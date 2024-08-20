"""
Provides definition of funl grammar
"""

from textx import metamodel_from_str

funl_grammar = """
    Model: statement *= Statement;

    Statement: FunctionDefinition | FunctionCall;

    FunctionDefinition: name=ID '=' (function=FunctionCall |
    code_block=CodeBlock);
    FunctionCall: name=ID '(' params*=Param (',' params*=Param)* ')';
    CodeBlock: '{' content=/[^{}]*/ '}';

    Param: FunctionCall| INT | ID | STRING;
    Comment: /#.*$/;
    ID: /[a-zA-Z_][a-zA-Z0-9_]*/;
    INT: /-?[0-9]+/;
    STRING: /".*"/;
"""

mm = metamodel_from_str(funl_grammar)
