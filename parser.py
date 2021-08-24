from lark import Lark

ExpressionParser = Lark(r"""
    ?node: atom
         |node OP atom
    ?atom: leaf
         |NT* "(" node ")"
    leaf: ID COMP literal
         |NT*  "(" leaf ")"
    NT: "NOT"i
    OP: "AND"i
      | "OR"i
    COMP: ">="
        | "<="
        | "!="
        | ">"
        | "<"
        | "=" 
    ID:   /\w+/
    literal: INT
           | DECIMAL
           | STRING
    STRING: "\""/.*?/"\""
    %import common.ESCAPED_STRING
    %import common.INT
    %import common.DECIMAL
    %import common.WS
    %ignore /\s+/
""",start='node', parser='lalr')
