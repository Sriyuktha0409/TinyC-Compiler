from sly import Parser
from Ast import *
from Function import *
from Program import *
from SymbolTable import *
from Lexer import lex
import argparse
apr=argparse.ArgumentParser()
apr.add_argument('-Ast',nargs=1)
args=apr.parse_args()
class parse(Parser):
    tokens = lex.tokens
    literals = lex.literals
    stable=SymbolTable()
    @_('return_type ID "(" ")" "{" statements "}" ')
    def program(self,value):
        prog = Program()
        fun = Function(value.return_type,value.ID)
        fun.setStatementsAstList(value.statements)
        fun.setLocalSymbolTable(self.stable.table)
        prog.addFunctionDetails(value[1],fun)
        if prog.getMainFunction() is None:
            print("Error: main function is not defined\n")
        else:
            with open(args.Ast[0]+'.ast','w') as v:
                prog.print(v)
    @_('INT')
    def return_type(self, value):
        return value[0]
    @_('statement ";" statements')
    def statements(self,value):
        return [value[0]] + value[2]
    @_('statement ";"')
    def statements(self,value):
        return [value[0]]
    @_('declaration_stmt','assignment_stmt','print_stmt')
    def statement(self,value):
        return value[0]
    @_('type list_of_variables')
    def declaration_stmt(self,value):
        for val in value[1]:
            if self.stable.nameInSymbolTable(val.symbolEntry)==False:
                v =SymbolTableEntry(val.symbolEntry,value[0])
                self.stable.addSymbol(v)
            else:
                print(f"Error: redeclaration of '{val.symbolEntry}'\n")
    @_('ID "," list_of_variables')
    def list_of_variables(self,value):
        return [NameAst(value[0])] + value[2]
    @_('ID')
    def list_of_variables(self,value):
        return [NameAst(value[0])]
    @_('ID "=" ID')
    def assignment_stmt(self,value):
        symentry=self.stable.getSymbolEntry(value[0])
        left=NameAst(symentry.name)
        symentry=self.stable.getSymbolEntry(value[2])
        right=NameAst(symentry.name)
        return AssignAst(left,right,value.lineno)
    @_('ID "=" CONST')
    def assignment_stmt(self,value):
        symentry=self.stable.getSymbolEntry(value[0])
        left=NameAst(symentry.name)
        return AssignAst(left,NumberAst(value[2]),value.lineno)
    @_('PRINT ID')
    def print_stmt(self,value):
        if self.stable.nameInSymbolTable(value[1])==False:
            print(f"Error: Variable {value[1]} not declared\n")
        else:
            return PrintAst(NameAst(value[1]))
    @_('INT')
    def type(self,value):
        return DataType.INT
lexer = lex()
parser = parse()
f= open(args.Ast[0])
expr= f.read()
obj = parser.parse(lexer.tokenize(expr))