from lark import Lark

ExpressionParser = Lark(r"""
?node: leaf | node OP node | "(" node ")"
leaf: ID COMP literal 
OP: "AND" | "OR"
COMP: ">=" | "<=" | "!=" | ">" | "<" | "=" 
ID:   /\w+/
literal: INT | DECIMAL | STRING
STRING: "\""/.*?/"\""
%import common.ESCAPED_STRING
%import common.INT
%import common.DECIMAL
%import common.WS
%ignore /\s+/
    """,start='node')