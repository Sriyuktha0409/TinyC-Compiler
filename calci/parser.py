from sly import Parser
from lexer import Calclexer
import argparse
apr= argparse.ArgumentParser()
apr.add_argument("filename")
apr.add_argument('-t',nargs=1)
args=apr.parse_args()
class calcParser(Parser):
    tokens=Calclexer.tokens
    literals=Calclexer.literals
    precedence=(('left',"+","-"),('left',"*","/"))
    @_('expr')
    def x(self,value):
        print(value[0])
    @_('x NEWLINE expr')
    def x(self,value):
        print(value[2])
    @_('expr "+" expr')
    def expr(self,value):
    	return value[0]+value[2]
    @_('expr "-" expr')
    def expr(self,value):
        return value[0]-value[2]
    @_('expr "*" expr')
    def expr(self,value):
    	return value[0]*value[2]
    @_('expr "/" expr')
    def expr(self,value):
        return value[0]/value[2]
    @_('"(" expr ")"')
    def expr(self,value):
    	return value[1]
    @_('INTEGER','ID')
    def expr(self,value):
        return value[0]
lexer=Calclexer()
parser=calcParser()
f=open(args.filename)
expr=f.read()
print('\tResult')
result=parser.parse(lexer.tokenize(expr))
print(result)