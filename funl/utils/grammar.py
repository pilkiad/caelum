"""
> funl grammar

This module contains the textx grammar that defines the funl programming
language. It is meant as a sort of lookup-table for the parser.
"""

grammar = """
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