from sly import Lexer
class lex(Lexer):
    literals = {"(",")",";","=","{","}",","}
    tokens = {ID,INT,PRINT,CONST}
    ignore = ' \t\n'
    ID=r'[a-zA-Z]+'
    CONST = r'[0-9]+'
    ID['print']=PRINT
    ID['int']=INT