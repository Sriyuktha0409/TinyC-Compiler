from sly import Parser
from Lexer import LexicalAnalyzer
from SymbolTable import SymbolTable, SymbolTableEntry
from Ast import *
from Program import Program
from Function import Function
from enum import Enum
DataType = Enum("DataType", ["INT", "DOUBLE"])
class Level2Parser(Parser):
    literals = LexicalAnalyzer.literals
    tokens = LexicalAnalyzer.tokens
    program = Program()
    localSymbolTable = SymbolTable()
    dataType = None
    isAccepted = True
    @_(' return_type ID "(" ")" "{" statements "}" ')
    def Program(self, value):
        function = Function(value.return_type, value.ID)
        function.setStatementsAstList([i for i in value.statements if i is not None])
        function.setLocalSymbolTable(self.localSymbolTable)
        self.program.addFunctionDetails(value.ID, function)
        return self.isAccepted
    @_(" INT ")
    def return_type(self, value):
        return DataType.INT.name
    @_(' statement ";" statements ')
    def statements(self, value):
        return [value.statement] + value.statements
    @_(' statement ";" ')
    def statements(self, value):
        return [value.statement]
    @_(" declaration ")
    def statement(self, value):
        pass
    @_("assignment", "print")
    def statement(self, value):
        return value[0]
    @_(" type LIST ")
    def declaration(self, value):
        pass
    @_(' ID "," LIST ')
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID,
        self.dataType,self.localSymbolTable.getLen()*-4))
    @_(' ID "=" NUMBER "," LIST ')
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID,
        self.dataType, self.localSymbolTable.getLen()*-4, value.NUMBER))
    @_(' ID "=" NUMBER ')
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID,
        self.dataType, self.localSymbolTable.getLen()*-4,value.NUMBER))
    @_(" ID ")
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID,self.dataType, self.localSymbolTable.getLen()*-4))
    @_(' ID "=" expr ')
    def assignment(self, value):
        if self.localSymbolTable.nameInSymbolTable(value.ID):
            lhs = NameAst(self.localSymbolTable.getSymbol(value.ID))
            ast = AssignAst(lhs, value.expr, value.lineno)
            if value.expr is not None:
                if ast.typeCheckAST():
                    return ast
                else:
                    print(f"Type is not matched at line {value.lineno}")
                    self.isAccepted = False
                    return None
            else:
                print(f"Symbol {value.ID} not been declared")
                self.isAccepted = False
                return
        else:
            print(f"Symbol {value.ID} not been declared")
            self.isAccepted = False
    @_(" PRINT expr ")
    def print(self, value):
        return PrintAst(value.expr)
    @_("NUMBER")
    def expr(self, value):
        return NumberAst(value.NUMBER)
    @_("ID")
    def expr(self, value):
        if self.localSymbolTable.nameInSymbolTable(value.ID):
            return NameAst(self.localSymbolTable.getSymbol(value.ID))
        else:
            print(f"Symbol {value.ID} not been declared")
            self.isAccepted = False
            return None
    @_('"(" expr ")"')
    def expr(self, value):
        return value.expr
    @_(" INT ")
    def type(self, value):
        self.dataType = DataType.INT.name